var STATUSES = [
  {id:'new',label:'Нові',color:'#2196f3'},
  {id:'contact',label:'Контакт',color:'#ff9800'},
  {id:'negotiations',label:'Переговори',color:'#9c27b0'},
  {id:'onboarding',label:'Онбординг',color:'#4caf50'},
  {id:'clients',label:'Клієнти',color:'#000'}
];

var ONBOARDING_STEPS = [
  'Договір підписано',
  'Товар прийнято на склад',
  'Інтеграція CRM налаштована',
  'Тестове відправлення',
  'Навчання менеджера',
  'Перший робочий день',
  'Перший тиждень — все ОК'
];

var TYPE_LABELS = {
  heavy:'Важкі товари',cosmetics:'Косметика',clothing:'Одяг/взуття',
  electronics:'Електроніка',food:'Продукти',other:'Інше'
};

var SOURCE_LABELS = {
  site:'Сайт',telegram:'Telegram',call:'Дзвінок',
  recommendation:'Рекомендація',ads:'Реклама',other:'Інше'
};

var defaultLeads = [
  {id:1,company:'EcoDrive',contact:'Олег Петренко',phone:'+380501234567',email:'oleg@ecodrive.ua',shipments:150,type:'heavy',source:'site',status:'negotiations',date:'2026-03-20',comments:[{text:'Важкі товари 50+ кг, обговорюємо тарифи',date:'2026-03-20 10:30'}],onboarding:[false,false,false,false,false,false,false]},
  {id:2,company:'OrnerUA',contact:'Марія Ковальчук',phone:'+380672345678',email:'maria@orner.ua',shipments:300,type:'other',source:'recommendation',status:'clients',date:'2026-01-15',comments:[{text:'Активний клієнт, все ок',date:'2026-01-15 14:00'}],onboarding:[true,true,true,true,true,true,true]},
  {id:3,company:'BeautyBox',contact:'Анна Сидоренко',phone:'+380933456789',email:'anna@beautybox.ua',shipments:80,type:'cosmetics',source:'telegram',status:'onboarding',date:'2026-03-18',comments:[{text:'Договір підписано, налаштовуємо інтеграцію',date:'2026-03-18 16:00'}],onboarding:[true,true,false,false,false,false,false]},
  {id:4,company:'FashionUA',contact:'Дмитро Лисенко',phone:'+380504567890',email:'dima@fashionua.com',shipments:200,type:'clothing',source:'site',status:'contact',date:'2026-03-22',comments:[],onboarding:[false,false,false,false,false,false,false]},
  {id:5,company:'TechStore',contact:'Ірина Мельник',phone:'+380675678901',email:'irina@techstore.ua',shipments:50,type:'electronics',source:'call',status:'new',date:'2026-03-23',comments:[],onboarding:[false,false,false,false,false,false,false]}
];

function getLeads(){
  var d=localStorage.getItem('mtp_crm_leads');
  if(!d){localStorage.setItem('mtp_crm_leads',JSON.stringify(defaultLeads));return defaultLeads.slice();}
  return JSON.parse(d);
}
function saveLeads(leads){localStorage.setItem('mtp_crm_leads',JSON.stringify(leads));}
function getSettings(){var d=localStorage.getItem('mtp_crm_settings');return d?JSON.parse(d):{};}
function saveSettings(s){localStorage.setItem('mtp_crm_settings',JSON.stringify(s));}
function nextId(leads){return leads.reduce(function(m,l){return Math.max(m,l.id);},0)+1;}

function getStatusLabel(id){
  var s=STATUSES.find(function(x){return x.id===id;});
  return s?s.label:id;
}

function notifyTelegram(msg){
  fetch('/api/telegram',{
    method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({text:msg,parse_mode:'HTML'})
  }).catch(function(){});
}

function notifyNewLead(lead){
  notifyTelegram(
    '\uD83C\uDD95 Нова заявка!\n'+
    '\uD83C\uDFE2 Компанія: '+lead.company+'\n'+
    '\uD83D\uDC64 Контакт: '+lead.contact+'\n'+
    '\uD83D\uDCF1 Телефон: '+lead.phone+'\n'+
    '\uD83D\uDCE6 Відправлень/день: '+lead.shipments+'\n'+
    '\uD83C\uDFF7 Тип: '+(TYPE_LABELS[lead.type]||lead.type)+'\n'+
    '\uD83D\uDCCB Джерело: '+(SOURCE_LABELS[lead.source]||lead.source)
  );
}

function notifyStatusChange(lead,oldStatus,newStatus){
  if(oldStatus===newStatus)return;
  notifyTelegram(
    '\uD83D\uDCCA Зміна статусу заявки\n'+
    '\uD83C\uDFE2 '+lead.company+'\n'+
    getStatusLabel(oldStatus)+' \u2192 '+getStatusLabel(newStatus)
  );
}

function renderBoard(){
  var leads=getLeads();
  STATUSES.forEach(function(s){
    var col=document.getElementById('col-'+s.id);
    if(!col)return;
    var items=leads.filter(function(l){return l.status===s.id;});
    var countEl=col.querySelector('.kanban-count');
    if(countEl)countEl.textContent=items.length;
    var body=col.querySelector('.kanban-body');
    if(!body)return;
    body.innerHTML=items.map(function(l){
      var done=l.onboarding.filter(Boolean).length;
      var progress=Math.round(done/7*100);
      return '<div class="kanban-card" onclick="openLead('+l.id+')" draggable="true" data-id="'+l.id+'">'+
        '<div class="kc-company">'+l.company+'</div>'+
        '<div class="kc-contact">'+l.contact+'</div>'+
        '<div class="kc-meta">'+l.shipments+' відпр/день &middot; '+(TYPE_LABELS[l.type]||l.type)+'</div>'+
        (s.id==='onboarding'||s.id==='clients'?'<div class="kc-progress"><div class="kc-progress-bar" style="width:'+progress+'%"></div></div><div class="kc-progress-text">'+done+'/7</div>':'')+
        '</div>';
    }).join('');
  });
  renderStats(leads);
}

function renderStats(leads){
  var el=document.getElementById('crmStats');
  if(!el)return;
  var total=leads.length;
  var newC=leads.filter(function(l){return l.status==='new';}).length;
  var clients=leads.filter(function(l){return l.status==='clients';}).length;
  var shipTotal=leads.reduce(function(s,l){return s+l.shipments;},0);
  el.innerHTML='<div class="card"><div class="card-value">'+total+'</div><div class="card-label">Всього заявок</div></div>'+
    '<div class="card"><div class="card-value">'+newC+'</div><div class="card-label">Нових</div></div>'+
    '<div class="card"><div class="card-value">'+clients+'</div><div class="card-label">Клієнтів</div></div>'+
    '<div class="card"><div class="card-value">'+shipTotal+'</div><div class="card-label">Відправлень/день</div></div>';
}

function openLead(id){
  var leads=getLeads();
  var lead=leads.find(function(l){return l.id===id;});
  if(!lead)return;
  var m=document.getElementById('leadModal');
  m.dataset.leadId=id;

  document.getElementById('lmCompany').value=lead.company;
  document.getElementById('lmContact').value=lead.contact;
  document.getElementById('lmPhone').value=lead.phone;
  document.getElementById('lmEmail').value=lead.email;
  document.getElementById('lmShipments').value=lead.shipments;
  document.getElementById('lmType').value=lead.type;
  document.getElementById('lmSource').value=lead.source;
  document.getElementById('lmStatus').value=lead.status;

  // Onboarding
  var obDiv=document.getElementById('lmOnboarding');
  obDiv.innerHTML=ONBOARDING_STEPS.map(function(step,i){
    return '<label class="ob-step"><input type="checkbox" data-step="'+i+'"'+(lead.onboarding[i]?' checked':'')+' onchange="toggleStep('+id+','+i+',this.checked)"> '+step+'</label>';
  }).join('');
  var done=lead.onboarding.filter(Boolean).length;
  document.getElementById('lmObProgress').textContent=done+' з 7 виконано';

  // Comments
  var cmDiv=document.getElementById('lmComments');
  cmDiv.innerHTML=lead.comments.map(function(c){
    return '<div class="comment"><div class="comment-date">'+c.date+'</div><div class="comment-text">'+c.text+'</div></div>';
  }).join('')||(('<div class="comment"><div class="comment-text" style="color:#888">Немає коментарів</div></div>'));

  document.getElementById('lmNewComment').value='';
  m.classList.add('show');
}

function closeLead(){document.getElementById('leadModal').classList.remove('show');}

function saveLead(){
  var m=document.getElementById('leadModal');
  var id=parseInt(m.dataset.leadId);
  var leads=getLeads();
  var lead=leads.find(function(l){return l.id===id;});
  if(!lead)return;
  var oldStatus=lead.status;
  lead.company=document.getElementById('lmCompany').value;
  lead.contact=document.getElementById('lmContact').value;
  lead.phone=document.getElementById('lmPhone').value;
  lead.email=document.getElementById('lmEmail').value;
  lead.shipments=parseInt(document.getElementById('lmShipments').value)||0;
  lead.type=document.getElementById('lmType').value;
  lead.source=document.getElementById('lmSource').value;
  lead.status=document.getElementById('lmStatus').value;
  notifyStatusChange(lead,oldStatus,lead.status);

  var cmt=document.getElementById('lmNewComment').value.trim();
  if(cmt){
    var now=new Date();
    lead.comments.push({text:cmt,date:now.toISOString().slice(0,10)+' '+now.toTimeString().slice(0,5)});
  }
  saveLeads(leads);
  closeLead();
  renderBoard();
}

function deleteLead(){
  if(!confirm('Видалити цю заявку?'))return;
  var m=document.getElementById('leadModal');
  var id=parseInt(m.dataset.leadId);
  var leads=getLeads().filter(function(l){return l.id!==id;});
  saveLeads(leads);
  closeLead();
  renderBoard();
}

function toggleStep(id,step,checked){
  var leads=getLeads();
  var lead=leads.find(function(l){return l.id===id;});
  if(!lead)return;
  lead.onboarding[step]=checked;
  saveLeads(leads);
  var done=lead.onboarding.filter(Boolean).length;
  document.getElementById('lmObProgress').textContent=done+' з 7 виконано';
}

function openNewLead(){
  document.getElementById('newLeadModal').classList.add('show');
  document.getElementById('nlCompany').value='';
  document.getElementById('nlContact').value='';
  document.getElementById('nlPhone').value='';
  document.getElementById('nlEmail').value='';
  document.getElementById('nlShipments').value='';
  document.getElementById('nlType').value='other';
  document.getElementById('nlSource').value='site';
}
function closeNewLead(){document.getElementById('newLeadModal').classList.remove('show');}

function saveNewLead(){
  var leads=getLeads();
  var now=new Date();
  var newLead={
    id:nextId(leads),
    company:document.getElementById('nlCompany').value,
    contact:document.getElementById('nlContact').value,
    phone:document.getElementById('nlPhone').value,
    email:document.getElementById('nlEmail').value,
    shipments:parseInt(document.getElementById('nlShipments').value)||0,
    type:document.getElementById('nlType').value,
    source:document.getElementById('nlSource').value,
    status:'new',
    date:now.toISOString().slice(0,10),
    comments:[],
    onboarding:[false,false,false,false,false,false,false]
  };
  leads.push(newLead);
  saveLeads(leads);
  notifyNewLead(newLead);
  closeNewLead();
  renderBoard();
}

function sendNotification(){
  var m=document.getElementById('leadModal');
  var id=parseInt(m.dataset.leadId);
  var leads=getLeads();
  var lead=leads.find(function(l){return l.id===id;});
  if(!lead)return;

  var channel=document.getElementById('lmNotifyChannel').value;
  var msg=document.getElementById('lmNotifyText').value||
    'Нова заявка MTP:\nКомпанія: '+lead.company+'\nКонтакт: '+lead.contact+'\nТел: '+lead.phone+'\nВідправлень/день: '+lead.shipments;

  if(channel==='telegram'){
    fetch('/api/telegram',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({text:msg,parse_mode:'HTML'})
    }).then(function(r){return r.json();}).then(function(d){
      alert(d.ok?'Надіслано в Telegram!':'Помилка відправки');
    }).catch(function(e){alert('Помилка: '+e.message);});
  } else {
    window.location.href='mailto:?subject=MTP CRM: '+lead.company+'&body='+encodeURIComponent(msg);
  }
}

function openSettings(){document.getElementById('settingsModal').classList.add('show');
  var s=getSettings();
  document.getElementById('stTgToken').value=s.tgToken||'';
  document.getElementById('stTgChat').value=s.tgChatId||'';
  document.getElementById('stEmail').value=s.notifyEmail||'';
}
function closeSettings(){document.getElementById('settingsModal').classList.remove('show');}
function saveSettingsForm(){
  saveSettings({
    tgToken:document.getElementById('stTgToken').value,
    tgChatId:document.getElementById('stTgChat').value,
    notifyEmail:document.getElementById('stEmail').value
  });
  alert('Налаштування збережено');
  closeSettings();
}
