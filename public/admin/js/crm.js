/* ========== CRM v2 — MTP Group ========== */

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

var TIMELINE_ICONS = {
  phone:'\uD83D\uDCDE',
  telegram:'\uD83D\uDCAC',
  email:'\u2709\uFE0F',
  meeting:'\uD83E\uDD1D'
};

var TIMELINE_LABELS = {
  phone:'Дзвінок',
  telegram:'Telegram',
  email:'Email',
  meeting:'Зустріч'
};

/* ===== ACTIVE FILTERS STATE ===== */
var activeFilters = {source:[], type:[]};

/* ===== DEFAULT DATA ===== */
var defaultLeads = [
  {id:1,company:'EcoDrive',contact:'Олег Петренко',phone:'+380501234567',email:'oleg@ecodrive.ua',shipments:150,type:'heavy',source:'site',status:'negotiations',date:'2026-03-20',nextContact:'2026-03-30',comments:[{text:'Важкі товари 50+ кг, обговорюємо тарифи',date:'2026-03-20 10:30'}],onboarding:[false,false,false,false,false,false,false],timeline:[{type:'phone',note:'Перший дзвінок — обговорення потреб',date:'2026-03-20 10:00'},{type:'email',note:'Надіслано комерційну пропозицію',date:'2026-03-21 14:30'}]},
  {id:2,company:'OrnerUA',contact:'Марія Ковальчук',phone:'+380672345678',email:'maria@orner.ua',shipments:300,type:'other',source:'recommendation',status:'clients',date:'2026-01-15',nextContact:'',comments:[{text:'Активний клієнт, все ок',date:'2026-01-15 14:00'}],onboarding:[true,true,true,true,true,true,true],timeline:[{type:'meeting',note:'Підписання договору',date:'2026-01-15 11:00'}]},
  {id:3,company:'BeautyBox',contact:'Анна Сидоренко',phone:'+380933456789',email:'anna@beautybox.ua',shipments:80,type:'cosmetics',source:'telegram',status:'onboarding',date:'2026-03-18',nextContact:'2026-03-31',comments:[{text:'Договір підписано, налаштовуємо інтеграцію',date:'2026-03-18 16:00'}],onboarding:[true,true,false,false,false,false,false],timeline:[{type:'telegram',note:'Перше звернення через Telegram',date:'2026-03-17 09:00'},{type:'phone',note:'Детальне обговорення умов',date:'2026-03-18 11:00'}]},
  {id:4,company:'FashionUA',contact:'Дмитро Лисенко',phone:'+380504567890',email:'dima@fashionua.com',shipments:200,type:'clothing',source:'site',status:'contact',date:'2026-03-22',nextContact:'2026-03-29',comments:[],onboarding:[false,false,false,false,false,false,false],timeline:[]},
  {id:5,company:'TechStore',contact:'Ірина Мельник',phone:'+380675678901',email:'irina@techstore.ua',shipments:50,type:'electronics',source:'call',status:'new',date:'2026-03-23',nextContact:'',comments:[],onboarding:[false,false,false,false,false,false,false],timeline:[]}
];

/* ===== STORAGE ===== */
var _leadsCache=null;
var _leadsLoading=false;

function getLeads(){
  // Return cache synchronously (for render)
  if(_leadsCache) return _leadsCache;
  // Fallback to localStorage while API loads
  var d=localStorage.getItem('mtp_crm_leads');
  if(!d) return defaultLeads.slice();
  var leads=JSON.parse(d);
  // Migration: add missing fields + fix site form leads
  leads.forEach(function(l){
    if(!l.timeline) l.timeline=[];
    if(l.nextContact===undefined) l.nextContact='';
    if(!l.company && !l.contact && l.phone) l.company='Заявка з сайту';
    if(!l.status) l.status='new';
    if(!l.source) l.source='site';
    if(!l.type) l.type='other';
    if(!l.comments) l.comments=[];
    if(!l.onboarding) l.onboarding=[false,false,false,false,false,false,false];
    if(!l.shipments) l.shipments=0;
    if(!l.email) l.email='';
    if(!l.contact) l.contact='';
    if(!l.date) l.date=new Date().toISOString().slice(0,10);
    if(typeof l.id !== 'number') l.id=Date.now()+Math.random();
  });
  return leads;
}
function saveLeads(leads){
  _leadsCache=leads;
  localStorage.setItem('mtp_crm_leads',JSON.stringify(leads));
  // Async save to API
  fetch('/api/leads',{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify(leads[leads.length-1]||{})}).catch(function(){});
}

function loadLeadsFromAPI(){
  if(_leadsLoading) return;
  _leadsLoading=true;
  fetch('/api/leads').then(function(r){return r.json();}).then(function(data){
    if(Array.isArray(data)&&data.length>0){
      _leadsCache=data;
      localStorage.setItem('mtp_crm_leads',JSON.stringify(data));
      renderBoard();
    }
    _leadsLoading=false;
  }).catch(function(){_leadsLoading=false;});
}
function getSettings(){var d=localStorage.getItem('mtp_crm_settings');return d?JSON.parse(d):{};}
function saveSettings(s){localStorage.setItem('mtp_crm_settings',JSON.stringify(s));}
function nextId(leads){return leads.reduce(function(m,l){return Math.max(m,l.id);},0)+1;}

function getStatusLabel(id){
  var s=STATUSES.find(function(x){return x.id===id;});
  return s?s.label:id;
}
function getStatusColor(id){
  var s=STATUSES.find(function(x){return x.id===id;});
  return s?s.color:'#888';
}

/* ===== TELEGRAM ===== */
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

/* ===== FILTERING ===== */
function getFilteredLeads(){
  var leads=getLeads();
  var q=(document.getElementById('crmSearch')||{}).value||'';
  q=q.toLowerCase().trim();
  if(q){
    leads=leads.filter(function(l){
      return (l.company||'').toLowerCase().indexOf(q)!==-1||
             (l.contact||'').toLowerCase().indexOf(q)!==-1||
             (l.phone||'').indexOf(q)!==-1;
    });
  }
  if(activeFilters.source.length>0){
    leads=leads.filter(function(l){return activeFilters.source.indexOf(l.source)!==-1;});
  }
  if(activeFilters.type.length>0){
    leads=leads.filter(function(l){return activeFilters.type.indexOf(l.type)!==-1;});
  }
  return leads;
}

function toggleFilter(btn){
  var filterType=btn.getAttribute('data-filter');
  var val=btn.getAttribute('data-value');
  var arr=activeFilters[filterType];
  var idx=arr.indexOf(val);
  if(idx===-1){arr.push(val);btn.classList.add('active');}
  else{arr.splice(idx,1);btn.classList.remove('active');}
  renderActiveChips();
  renderBoard();
}

function removeFilter(filterType,val){
  var arr=activeFilters[filterType];
  var idx=arr.indexOf(val);
  if(idx!==-1) arr.splice(idx,1);
  // Update button state
  var btns=document.querySelectorAll('.crm-filter-btn[data-filter="'+filterType+'"][data-value="'+val+'"]');
  btns.forEach(function(b){b.classList.remove('active');});
  renderActiveChips();
  renderBoard();
}

function renderActiveChips(){
  var el=document.getElementById('activeFilters');
  if(!el) return;
  var html='';
  activeFilters.source.forEach(function(v){
    html+='<span class="crm-chip" onclick="removeFilter(\'source\',\''+v+'\')">'+(SOURCE_LABELS[v]||v)+' <span class="chip-x">&times;</span></span>';
  });
  activeFilters.type.forEach(function(v){
    html+='<span class="crm-chip" onclick="removeFilter(\'type\',\''+v+'\')">'+(TYPE_LABELS[v]||v)+' <span class="chip-x">&times;</span></span>';
  });
  el.innerHTML=html;
}

function applyFilters(){renderBoard();}

/* ===== DATE HELPERS ===== */
function todayStr(){return new Date().toISOString().slice(0,10);}

function getDateBadgeClass(dateStr){
  if(!dateStr) return '';
  var today=todayStr();
  if(dateStr<today) return 'overdue';
  if(dateStr===today) return 'today';
  return 'future';
}

function formatDateBadge(dateStr){
  if(!dateStr) return '';
  var cls=getDateBadgeClass(dateStr);
  var labels={overdue:'Прострочено',today:'Сьогодні',future:''};
  var d=dateStr.split('-');
  var display=d[2]+'.'+d[1];
  var prefix=labels[cls]?labels[cls]+' ':'';
  return '<span class="kc-date-badge '+cls+'">'+prefix+display+'</span>';
}

/* ===== RENDER BOARD ===== */
function renderBoard(){
  var leads=getFilteredLeads();
  var allLeads=getLeads();

  STATUSES.forEach(function(s){
    var col=document.getElementById('col-'+s.id);
    if(!col)return;
    var items=leads.filter(function(l){return l.status===s.id;});
    var countEl=col.querySelector('.kanban-count');
    if(countEl)countEl.textContent=items.length;
    var body=col.querySelector('.kanban-body');
    if(!body)return;
    body.innerHTML=items.map(function(l){
      var done=l.onboarding?l.onboarding.filter(Boolean).length:0;
      var progress=Math.round(done/7*100);
      var dateBadge=formatDateBadge(l.nextContact);
      var sourceBadge='<span class="kc-source-badge">'+(SOURCE_LABELS[l.source]||l.source)+'</span>';
      return '<div class="kanban-card" data-id="'+l.id+'" onclick="openLead(\''+l.id+'\')">'+
        '<div class="kc-company">'+esc(l.company)+'</div>'+
        '<div class="kc-contact">'+esc(l.contact)+'</div>'+
        '<div class="kc-meta">'+l.shipments+' відпр/день &middot; '+(TYPE_LABELS[l.type]||l.type)+'</div>'+
        '<div class="kc-badges">'+sourceBadge+dateBadge+'</div>'+
        (s.id==='onboarding'||s.id==='clients'?'<div class="kc-progress"><div class="kc-progress-bar" style="width:'+progress+'%"></div></div><div class="kc-progress-text">'+done+'/7</div>':'')+
        '</div>';
    }).join('');
  });

  renderStats(allLeads);
  renderFunnel(allLeads);
  renderTodayBar(allLeads);
  initDragDrop();
}

function esc(s){
  if(!s) return '';
  var d=document.createElement('div');
  d.textContent=s;
  return d.innerHTML;
}

/* ===== STATS ===== */
function renderStats(leads){
  var el=document.getElementById('crmStats');
  if(!el)return;
  var total=leads.length;
  var newC=leads.filter(function(l){return l.status==='new';}).length;
  var clients=leads.filter(function(l){return l.status==='clients';}).length;
  var shipTotal=leads.reduce(function(s,l){return s+l.shipments;},0);
  // This week's new leads
  var now=new Date();
  var weekAgo=new Date(now);weekAgo.setDate(weekAgo.getDate()-7);
  var weekStr=weekAgo.toISOString().slice(0,10);
  var weekNew=leads.filter(function(l){return l.date>=weekStr;}).length;
  // Overdue contacts
  var today=todayStr();
  var overdue=leads.filter(function(l){return l.nextContact && l.nextContact<today;}).length;

  el.innerHTML=
    '<div class="card"><div class="card-value">'+total+'</div><div class="card-label">Всього заявок</div></div>'+
    '<div class="card"><div class="card-value">'+newC+'</div><div class="card-label">Нових</div></div>'+
    '<div class="card"><div class="card-value">'+clients+'</div><div class="card-label">Клієнтів</div></div>'+
    '<div class="card"><div class="card-value">'+shipTotal+'</div><div class="card-label">Відправлень/день</div></div>'+
    '<div class="card"><div class="card-value">'+weekNew+'</div><div class="card-label">Нових за тиждень</div></div>'+
    '<div class="card"><div class="card-value">'+(overdue>0?'<span class="card-overdue-badge">'+overdue+'</span>':'\u2014')+'</div><div class="card-label">Прострочені контакти</div></div>';
}

/* ===== FUNNEL ===== */
function renderFunnel(leads){
  var el=document.getElementById('crmFunnel');
  if(!el)return;
  var total=leads.length||1;
  var html='<div class="crm-funnel-title">Воронка конверсії</div><div class="crm-funnel">';
  var labelsHtml='<div class="crm-funnel-labels">';
  STATUSES.forEach(function(s){
    var count=leads.filter(function(l){return l.status===s.id;}).length;
    var pct=Math.max(count/total*100,5);
    html+='<div class="crm-funnel-seg" style="flex:'+pct+';background:'+s.color+';height:100%"><span>'+count+'</span></div>';
    labelsHtml+='<div class="crm-funnel-label" style="flex:'+pct+'">'+s.label+'</div>';
  });
  html+='</div>'+labelsHtml+'</div>';
  el.innerHTML=html;
}

/* ===== TODAY BAR ===== */
function renderTodayBar(leads){
  var bar=document.getElementById('crmTodayBar');
  var txt=document.getElementById('crmTodayText');
  if(!bar||!txt)return;
  var today=todayStr();
  var todayLeads=leads.filter(function(l){return l.nextContact===today;});
  if(todayLeads.length>0){
    bar.style.display='flex';
    txt.textContent='Сьогодні контакти: '+todayLeads.length+' — '+todayLeads.map(function(l){return l.company;}).join(', ');
  } else {
    bar.style.display='none';
  }
}

/* ===== DRAG & DROP ===== */
var draggedCardId=null;

function initDragDrop(){
  var cards=document.querySelectorAll('.kanban-card');
  var bodies=document.querySelectorAll('.kanban-body');

  cards.forEach(function(card){
    var isDragging=false;
    // Click handler - open lead card
    card.addEventListener('click',function(){
      if(isDragging)return;
      var id=parseInt(card.getAttribute('data-id'));
      if(id) openLead(id);
    });
    // Drag handlers (desktop only)
    card.setAttribute('draggable','true');
    card.addEventListener('dragstart',function(e){
      isDragging=true;
      draggedCardId=parseInt(card.getAttribute('data-id'));
      card.classList.add('dragging');
      e.dataTransfer.effectAllowed='move';
      e.dataTransfer.setData('text/plain',String(draggedCardId));
    });
    card.addEventListener('dragend',function(){
      setTimeout(function(){isDragging=false;},100);
      card.classList.remove('dragging');
      draggedCardId=null;
      document.querySelectorAll('.kanban-col').forEach(function(c){c.classList.remove('drag-over');});
    });
  });

  bodies.forEach(function(body){
    body.addEventListener('dragover',function(e){
      e.preventDefault();
      e.dataTransfer.dropEffect='move';
      var col=body.closest('.kanban-col');
      if(col) col.classList.add('drag-over');
    });
    body.addEventListener('dragleave',function(e){
      var col=body.closest('.kanban-col');
      if(col && !col.contains(e.relatedTarget)) col.classList.remove('drag-over');
    });
    body.addEventListener('drop',function(e){
      e.preventDefault();
      var col=body.closest('.kanban-col');
      if(col) col.classList.remove('drag-over');
      var newStatus=body.getAttribute('data-status');
      if(!draggedCardId||!newStatus)return;

      var leads=getLeads();
      var lead=leads.find(function(l){return String(l.id)===String(draggedCardId);});
      if(!lead)return;
      var oldStatus=lead.status;
      if(oldStatus===newStatus)return;

      lead.status=newStatus;
      saveLeads(leads);
      notifyStatusChange(lead,oldStatus,newStatus);
      renderBoard();
    });
  });
}

/* ===== OPEN LEAD MODAL ===== */
function openLead(id){
  console.log('openLead called with id:', id, typeof id);
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
  if(!lead){console.error('Lead not found:',id);return;}
  
  // Ensure all fields exist
  lead.company=lead.company||'';
  lead.contact=lead.contact||'';
  lead.phone=lead.phone||'';
  lead.email=lead.email||'';
  lead.shipments=lead.shipments||0;
  lead.type=lead.type||'other';
  lead.source=lead.source||'site';
  lead.status=lead.status||'new';
  lead.nextContact=lead.nextContact||'';
  lead.onboarding=lead.onboarding||[false,false,false,false,false,false,false];
  lead.timeline=lead.timeline||[];
  lead.comments=lead.comments||[];

  var m=document.getElementById('leadModal');
  if(!m){console.error('leadModal not found');return;}
  m.dataset.leadId=id;

  var el;
  el=document.getElementById('lmTitle');if(el)el.textContent=lead.company||'Заявка #'+lead.id;
  el=document.getElementById('lmCompany');if(el)el.value=lead.company;
  el=document.getElementById('lmContact');if(el)el.value=lead.contact;
  el=document.getElementById('lmPhone');if(el)el.value=lead.phone;
  el=document.getElementById('lmEmail');if(el)el.value=lead.email;
  el=document.getElementById('lmShipments');if(el)el.value=lead.shipments;
  el=document.getElementById('lmType');if(el)el.value=lead.type;
  el=document.getElementById('lmSource');if(el)el.value=lead.source;
  el=document.getElementById('lmNextContact');if(el)el.value=lead.nextContact;

  el=document.getElementById('lmPhoneLink');if(el)el.href=lead.phone?'tel:'+lead.phone:'#';
  el=document.getElementById('lmEmailLink');if(el)el.href=lead.email?'mailto:'+lead.email:'#';

  el=document.getElementById('lmStatusPills');
  if(el)el.innerHTML=STATUSES.map(function(s){
    var active=lead.status===s.id?' active':'';
    return '<span class="status-pill'+active+'" style="background:'+s.color+';color:#fff" data-status="'+s.id+'" onclick="quickStatusChange(\''+s.id+'\')">'+s.label+'</span>';
  }).join('');

  el=document.getElementById('lmOnboarding');
  if(el)el.innerHTML=ONBOARDING_STEPS.map(function(step,i){
    var checked=lead.onboarding&&lead.onboarding[i]?' checked':'';
    return '<label class="ob-step"><input type="checkbox"'+checked+' onchange="toggleStep('+id+','+i+',this.checked)"> '+step+'</label>';
  }).join('');
  
  var done=(lead.onboarding||[]).filter(Boolean).length;
  el=document.getElementById('lmObProgress');if(el)el.textContent=done+' з 7 виконано';

  renderTimeline(lead);
  renderComments(lead);

  el=document.getElementById('lmNewComment');if(el)el.value='';
  el=document.getElementById('lmTimelineNote');if(el)el.value='';

  console.log('Opening modal now');
  m.classList.add('show');
  console.log('Modal should be visible, classList:', m.classList.toString());
}

function quickStatusChange(newStatus){
  var m=document.getElementById('leadModal');
  var id=m.dataset.leadId;
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
  if(!lead)return;
  var oldStatus=lead.status;
  lead.status=newStatus;
  saveLeads(leads);
  notifyStatusChange(lead,oldStatus,newStatus);
  // Re-render pills
  var pillsEl=document.getElementById('lmStatusPills');
  pillsEl.querySelectorAll('.status-pill').forEach(function(p){
    p.classList.toggle('active',p.getAttribute('data-status')===newStatus);
  });
  renderBoard();
}

function renderTimeline(lead){
  var el=document.getElementById('lmTimeline');
  if(!el)return;
  if(!lead.timeline||lead.timeline.length===0){
    el.innerHTML='<div class="timeline-empty">Немає записів</div>';
    return;
  }
  var sorted=lead.timeline.slice().sort(function(a,b){return a.date>b.date?-1:1;});
  el.innerHTML='<div class="timeline-list">'+sorted.map(function(t){
    return '<div class="timeline-entry">'+
      '<div class="timeline-icon">'+(TIMELINE_ICONS[t.type]||'')+'</div>'+
      '<div class="timeline-body">'+
        '<div class="timeline-date">'+t.date+' &middot; '+(TIMELINE_LABELS[t.type]||t.type)+'</div>'+
        '<div class="timeline-note">'+esc(t.note)+'</div>'+
      '</div>'+
    '</div>';
  }).join('')+'</div>';
}

function renderComments(lead){
  var cmDiv=document.getElementById('lmComments');
  if(!cmDiv)return;
  if(!lead.comments||lead.comments.length===0){
    cmDiv.innerHTML='<div class="comments-empty">Немає коментарів</div>';
    return;
  }
  var sorted=lead.comments.slice().sort(function(a,b){return a.date>b.date?-1:1;});
  cmDiv.innerHTML='<div class="comments-list">'+sorted.map(function(c){
    return '<div class="comment"><div class="comment-date">'+c.date+'</div><div class="comment-text">'+esc(c.text)+'</div></div>';
  }).join('')+'</div>';
}

function addTimelineEntry(){
  var m=document.getElementById('leadModal');
  var id=m.dataset.leadId;
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
  if(!lead)return;
  var note=document.getElementById('lmTimelineNote').value.trim();
  if(!note)return;
  var type=document.getElementById('lmTimelineType').value;
  var now=new Date();
  var dateStr=now.toISOString().slice(0,10)+' '+now.toTimeString().slice(0,5);
  if(!lead.timeline) lead.timeline=[];
  lead.timeline.push({type:type,note:note,date:dateStr});
  saveLeads(leads);
  document.getElementById('lmTimelineNote').value='';
  renderTimeline(lead);
}

function addCommentFromModal(){
  var m=document.getElementById('leadModal');
  var id=m.dataset.leadId;
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
  if(!lead)return;
  var cmt=document.getElementById('lmNewComment').value.trim();
  if(!cmt)return;
  var now=new Date();
  lead.comments.push({text:cmt,date:now.toISOString().slice(0,10)+' '+now.toTimeString().slice(0,5)});
  saveLeads(leads);
  document.getElementById('lmNewComment').value='';
  renderComments(lead);
}

function closeLead(){document.getElementById('leadModal').classList.remove('show');}

function saveLead(){
  var m=document.getElementById('leadModal');
  var id=m.dataset.leadId;
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
  if(!lead)return;
  var oldStatus=lead.status;
  lead.company=document.getElementById('lmCompany').value;
  lead.contact=document.getElementById('lmContact').value;
  lead.phone=document.getElementById('lmPhone').value;
  lead.email=document.getElementById('lmEmail').value;
  lead.shipments=parseInt(document.getElementById('lmShipments').value)||0;
  lead.type=document.getElementById('lmType').value;
  lead.source=document.getElementById('lmSource').value;
  lead.nextContact=document.getElementById('lmNextContact').value||'';

  // Status from pills (current active pill)
  var activePill=document.querySelector('#lmStatusPills .status-pill.active');
  if(activePill){
    lead.status=activePill.getAttribute('data-status');
  }
  notifyStatusChange(lead,oldStatus,lead.status);

  var cmt=document.getElementById('lmNewComment').value.trim();
  if(cmt){
    var now=new Date();
    lead.comments.push({text:cmt,date:now.toISOString().slice(0,10)+' '+now.toTimeString().slice(0,5)});
  }
  // Save to API
  fetch('/api/leads',{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify(lead)}).catch(function(){});
  saveLeads(leads);
  closeLead();
  renderBoard();
}

function deleteLead(){
  if(!confirm('Видалити цю заявку?'))return;
  var m=document.getElementById('leadModal');
  var id=m.dataset.leadId;
  fetch('/api/leads?id='+id,{method:'DELETE'}).catch(function(){});
  var leads=getLeads().filter(function(l){return String(l.id)!==String(id);});
  saveLeads(leads);
  closeLead();
  renderBoard();
}

function toggleStep(id,step,checked){
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
  if(!lead)return;
  lead.onboarding[step]=checked;
  saveLeads(leads);
  var done=lead.onboarding.filter(Boolean).length;
  document.getElementById('lmObProgress').textContent=done+' з 7 виконано';
}

/* ===== NEW LEAD ===== */
function openNewLead(){
  document.getElementById('newLeadModal').classList.add('show');
  document.getElementById('nlCompany').value='';
  document.getElementById('nlContact').value='';
  document.getElementById('nlPhone').value='';
  document.getElementById('nlEmail').value='';
  document.getElementById('nlShipments').value='';
  document.getElementById('nlType').value='other';
  document.getElementById('nlSource').value='site';
  document.getElementById('nlNextContact').value='';
}
function closeNewLead(){document.getElementById('newLeadModal').classList.remove('show');}

function saveNewLead(){
  var company=document.getElementById('nlCompany').value.trim();
  if(!company){alert('Введіть назву компанії');return;}
  var leads=getLeads();
  var now=new Date();
  var newLead={
    id:nextId(leads),
    company:company,
    contact:document.getElementById('nlContact').value,
    phone:document.getElementById('nlPhone').value,
    email:document.getElementById('nlEmail').value,
    shipments:parseInt(document.getElementById('nlShipments').value)||0,
    type:document.getElementById('nlType').value,
    source:document.getElementById('nlSource').value,
    status:'new',
    date:now.toISOString().slice(0,10),
    nextContact:document.getElementById('nlNextContact').value||'',
    comments:[],
    onboarding:[false,false,false,false,false,false,false],
    timeline:[]
  };
  fetch('/api/leads',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(newLead)}).then(function(r){return r.json();}).then(function(saved){if(saved.id)newLead.id=saved.id;}).catch(function(){});
  leads.push(newLead);
  saveLeads(leads);
  notifyNewLead(newLead);
  closeNewLead();
  renderBoard();
}

/* ===== NOTIFICATIONS ===== */
function sendNotification(){
  var m=document.getElementById('leadModal');
  var id=m.dataset.leadId;
  var leads=getLeads();
  var lead=leads.find(function(l){return String(l.id)===String(id);});
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

/* ===== CSV EXPORT ===== */
function exportCSV(){
  var leads=getLeads();
  var header=['Компанія','Контакт','Телефон','Email','Відправлень/день','Тип','Джерело','Статус','Наступний контакт','Дата'];
  var rows=leads.map(function(l){
    return [
      csvCell(l.company),
      csvCell(l.contact),
      csvCell(l.phone),
      csvCell(l.email),
      l.shipments,
      csvCell(TYPE_LABELS[l.type]||l.type),
      csvCell(SOURCE_LABELS[l.source]||l.source),
      csvCell(getStatusLabel(l.status)),
      csvCell(l.nextContact||''),
      csvCell(l.date)
    ].join(',');
  });
  var csv='\uFEFF'+header.join(',')+'\n'+rows.join('\n');
  var blob=new Blob([csv],{type:'text/csv;charset=utf-8;'});
  var url=URL.createObjectURL(blob);
  var a=document.createElement('a');
  a.href=url;
  a.download='mtp-crm-leads-'+todayStr()+'.csv';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function csvCell(val){
  val=String(val||'');
  if(val.indexOf(',')!==-1||val.indexOf('"')!==-1||val.indexOf('\n')!==-1){
    return '"'+val.replace(/"/g,'""')+'"';
  }
  return val;
}

/* ===== SETTINGS ===== */
function openSettings(){
  document.getElementById('settingsModal').classList.add('show');
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

/* ===== KEYBOARD SHORTCUTS ===== */
document.addEventListener('keydown',function(e){
  if(e.key==='Escape'){
    closeLead();
    closeNewLead();
    closeSettings();
  }
});


/* Manual refresh only — click Оновити button */
