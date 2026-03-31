(function(){
// Phone mask for ALL tel inputs on page (Tilda + custom)
function applyMask(inp){
  inp.addEventListener('input',function(){
    var v=this.value.replace(/\D/g,'');
    if(v.startsWith('380'))v=v.slice(2);
    else if(v.startsWith('38'))v=v.slice(2);
    else if(v.startsWith('80'))v='0'+v.slice(2);
    var m='+38 (';
    if(v.length>0)m+=v.substring(0,3);
    if(v.length>=3)m+=') ';
    if(v.length>3)m+=v.substring(3,6);
    if(v.length>=6)m+=' ';
    if(v.length>6)m+=v.substring(6,8);
    if(v.length>=8)m+=' ';
    if(v.length>8)m+=v.substring(8,10);
    this.value=m;
  });
  inp.addEventListener('focus',function(){if(!this.value||this.value.length<5)this.value='+38 (';});
  inp.addEventListener('blur',function(){if(this.value==='+38 ('||this.value==='+38 (0')this.value='';});
  inp.setAttribute('maxlength','19');
  inp.setAttribute('inputmode','tel');
}

// Apply to all phone inputs after DOM ready
function init(){
  // Find all tel inputs (Tilda uses type=tel or has Phone in name)
  document.querySelectorAll('input[type="tel"],input[name="Phone"],input[name="phone"]').forEach(applyMask);
  
  // Also find Tilda inputs with phone mask attribute
  document.querySelectorAll('input[data-tilda-rule="phone"]').forEach(applyMask);

  // Watch for Tilda dynamically adding inputs (popups)
  var obs=new MutationObserver(function(muts){
    muts.forEach(function(m){
      m.addedNodes.forEach(function(n){
        if(n.querySelectorAll){
          n.querySelectorAll('input[type="tel"],input[name="Phone"],input[data-tilda-rule="phone"]').forEach(applyMask);
        }
      });
    });
  });
  obs.observe(document.body,{childList:true,subtree:true});

  // Intercept Tilda form success → CRM + Telegram + redirect
  var sent={};
  function checkSuccess(){
    var boxes=document.querySelectorAll('.t-form__successbox');
    boxes.forEach(function(box){
      if(box.offsetParent===null||box.style.display==='none')return;
      var fid=box.closest('[id]');
      var key=fid?fid.id:'f';
      if(sent[key])return;
      sent[key]=true;

      // Get phone from nearest form
      var ph='';
      var form=box.closest('form')||box.closest('[data-formactiontype]');
      if(form){
        var tel=form.querySelector('input[type="tel"],input[name="Phone"],input[name="phone"]');
        if(tel)ph=tel.value;
      }
      if(!ph){
        var anyTel=document.querySelector('input[type="tel"]');
        if(anyTel)ph=anyTel.value;
      }

      // Save to CRM
      var leads=JSON.parse(localStorage.getItem('mtp_crm_leads')||'[]');
      leads.push({
        id:Date.now(),company:'Заявка з сайту',contact:'',phone:ph,email:'',
        shipments:0,type:'other',source:'Сайт — '+location.pathname,status:'new',
        date:new Date().toISOString().split('T')[0],
        comments:[{text:'Форма: '+location.pathname,date:new Date().toLocaleString('uk-UA')}],
        onboarding:[false,false,false,false,false,false,false]
      });
      localStorage.setItem('mtp_crm_leads',JSON.stringify(leads));

      // Telegram (server-side)
      fetch('/api/telegram',{
        method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({phone:ph,page:location.pathname})
      }).catch(function(){});

      // Redirect
      var isUA=location.pathname.indexOf('/ua/')===0||location.pathname==='/';
      setTimeout(function(){
        window.location.href=isUA?'/ua/thanks/':'/thanks/';
      },1500);
    });
  }

  // Watch for Tilda success boxes appearing
  var formObs=new MutationObserver(checkSuccess);
  formObs.observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['style','class']});
}

if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init);}else{init();}
})();
