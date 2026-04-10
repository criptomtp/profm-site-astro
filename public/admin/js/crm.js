/* ========== CRM v4 — MTP Group (Redis API) ========== */

var STATUSES = [
  {id:'new',label:'Нові',color:'#2196f3'},
  {id:'contact',label:'Контакт',color:'#ff9800'},
  {id:'meeting',label:'Зустріч',color:'#00bcd4'},
  {id:'negotiations',label:'Переговори',color:'#9c27b0'},
  {id:'onboarding',label:'Онбординг',color:'#4caf50'},
  {id:'clients',label:'Клієнти',color:'#000'},
  {id:'not_target',label:'Не наша ЦА',color:'#9e9e9e'},
  {id:'buyout',label:'Викуп товару',color:'#795548'}
];

var TYPE_LABELS = {heavy:'Важкі товари',cosmetics:'Косметика',clothing:'Одяг/взуття',electronics:'Електроніка',food:'Продукти',other:'Інше'};
var SOURCE_LABELS = {site:'Сайт',telegram:'Telegram',call:'Дзвінок',recommendation:'Рекомендація',ads:'Реклама',other:'Інше'};

var leads = [];
var currentLeadId = null;

/* ===== API ===== */
function apiGet(){
  return fetch('/api/leads').then(function(r){return r.json();}).then(function(data){
    if(Array.isArray(data)) leads = data;
    return leads;
  }).catch(function(){
    var d = localStorage.getItem('mtp_crm_leads');
    if(d) leads = JSON.parse(d);
    return leads;
  });
}
function apiPost(lead){return fetch('/api/leads',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(lead)}).then(function(r){return r.json();}).catch(function(){return lead;});}
function apiPut(lead){return fetch('/api/leads',{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify(lead)}).catch(function(){});}
function apiDelete(id){return fetch('/api/leads?id='+id,{method:'DELETE'}).catch(function(){});}
function saveLocal(){localStorage.setItem('mtp_crm_leads',JSON.stringify(leads));}

/* ===== RENDER ===== */
function renderBoard(){
  STATUSES.forEach(function(s){
    var col = document.getElementById('col-'+s.id);
    if(!col) return;
    var items = leads.filter(function(l){return l.status===s.id;});
    col.querySelector('.kanban-count').textContent = items.length;
    var body = col.querySelector('.kanban-body');
    body.innerHTML = items.map(function(l){
      var tgIcon = l.telegram ? ' · <a href="https://t.me/'+l.telegram.replace('@','')+'" target="_blank" style="color:#0088cc" onclick="event.stopPropagation()">💬</a>' : '';
      return '<div class="kanban-card" data-id="'+l.id+'">' +
        '<div class="kc-company">'+(l.company||l.phone||'Без назви')+'</div>' +
        '<div class="kc-contact">'+(l.contact||'')+'</div>' +
        '<div class="kc-meta">'+(l.phone||'')+tgIcon+
        (l.meetingDate?' · 📅 '+l.meetingDate.slice(0,10):'')+
        '</div></div>';
    }).join('');
  });
  document.querySelectorAll('.kanban-card').forEach(function(card){
    card.addEventListener('click',function(){openLead(card.getAttribute('data-id'));});
  });
  renderStats();
}

function renderStats(){
  var el = document.getElementById('crmStats');
  if(!el) return;
  el.innerHTML =
    '<div class="card"><div class="card-value">'+leads.length+'</div><div class="card-label">Всього</div></div>'+
    '<div class="card"><div class="card-value">'+leads.filter(function(l){return l.status==='new';}).length+'</div><div class="card-label">Нових</div></div>'+
    '<div class="card"><div class="card-value">'+leads.filter(function(l){return l.status==='meeting';}).length+'</div><div class="card-label">Зустрічей</div></div>'+
    '<div class="card"><div class="card-value">'+leads.filter(function(l){return l.status==='clients';}).length+'</div><div class="card-label">Клієнтів</div></div>';
}

/* ===== OPEN LEAD ===== */
function openLead(id){
  var lead = leads.find(function(l){return String(l.id)===String(id);});
  if(!lead){alert('Лід не знайдений');return;}
  currentLeadId = id;

  document.getElementById('lmTitle').textContent = lead.company||lead.phone||'Заявка';
  document.getElementById('lmCompany').value = lead.company||'';
  document.getElementById('lmContact').value = lead.contact||'';
  document.getElementById('lmPhone').value = lead.phone||'';
  document.getElementById('lmEmail').value = lead.email||'';
  document.getElementById('lmShipments').value = lead.shipments||0;
  document.getElementById('lmType').value = lead.type||'other';
  document.getElementById('lmSource').value = lead.source||'site';
  document.getElementById('lmStatus').value = lead.status||'new';
  document.getElementById('lmMeetingDate').value = lead.meetingDate||'';
  document.getElementById('lmMeetingLink').value = lead.meetingLink||'';
  document.getElementById('lmTelegram').value = lead.telegram||'';
  document.getElementById('lmTelegramGroup').value = lead.telegramGroup||'';

  // Telegram links
  var tgLink = document.getElementById('lmTgLink');
  var tgGroupLink = document.getElementById('lmTgGroupLink');
  if(tgLink){
    var tg = lead.telegram||'';
    if(tg){tgLink.href='https://t.me/'+tg.replace('@','');tgLink.style.display='';}
    else{tgLink.href='#';tgLink.style.display='none';}
  }
  if(tgGroupLink){
    var tgG = lead.telegramGroup||'';
    if(tgG){tgGroupLink.href=tgG.startsWith('http')?tgG:'https://t.me/'+tgG;tgGroupLink.style.display='';}
    else{tgGroupLink.href='#';tgGroupLink.style.display='none';}
  }

  // Update links on input change
  document.getElementById('lmTelegram').oninput=function(){
    var v=this.value.trim();
    if(tgLink){tgLink.href=v?'https://t.me/'+v.replace('@',''):'#';tgLink.style.display=v?'':'none';}
  };
  document.getElementById('lmTelegramGroup').oninput=function(){
    var v=this.value.trim();
    if(tgGroupLink){tgGroupLink.href=v?(v.startsWith('http')?v:'https://t.me/'+v):'#';tgGroupLink.style.display=v?'':'none';}
  };

  renderFiles(lead);
  renderComments(lead);
  document.getElementById('lmNewComment').value = '';
  document.getElementById('leadModal').classList.add('show');
}

function renderFiles(lead){
  var el = document.getElementById('lmFiles');
  var files = lead.files||[];
  el.innerHTML = files.length ? files.map(function(f){
    var icon = f.includes('drive.google')?'📁':f.includes('.pdf')?'📄':'🔗';
    var name = f.replace(/https?:\/\//,'').slice(0,40);
    return '<a href="'+f+'" target="_blank" class="file-link">'+icon+' '+name+'</a>';
  }).join('') : '<p style="color:#999;font-size:13px">Немає файлів</p>';
}

function renderComments(lead){
  var el = document.getElementById('lmComments');
  var comments = (lead.comments||[]).slice().reverse();
  el.innerHTML = comments.length ? comments.map(function(c){
    return '<div class="comment"><div class="comment-date">'+(c.date||'')+'</div><div class="comment-text">'+(c.text||'')+'</div></div>';
  }).join('') : '<p style="color:#999;font-size:13px">Немає коментарів</p>';
}

function addFile(){
  var input = document.getElementById('lmNewFile');
  var url = input.value.trim();
  if(!url) return;
  var lead = leads.find(function(l){return String(l.id)===String(currentLeadId);});
  if(!lead) return;
  if(!lead.files) lead.files=[];
  lead.files.push(url);
  apiPut(lead); saveLocal();
  input.value = '';
  renderFiles(lead);
}

function addCommentOnly(){
  var lead = leads.find(function(l){return String(l.id)===String(currentLeadId);});
  if(!lead) return;
  var cmt = document.getElementById('lmNewComment').value.trim();
  if(!cmt) return;
  if(!lead.comments) lead.comments=[];
  lead.comments.push({text:cmt, date:new Date().toLocaleString('uk-UA')});
  apiPut(lead); saveLocal();
  document.getElementById('lmNewComment').value = '';
  renderComments(lead);
}

function getMeetingDates(){
  var d = document.getElementById('lmMeetingDate').value;
  if(!d) return '';
  var start = d.replace(/[-:]/g,'').replace('T','T')+'00';
  var end = new Date(new Date(d).getTime()+3600000);
  var endStr = end.toISOString().replace(/[-:]/g,'').slice(0,15)+'00';
  return start+'/'+endStr;
}

function closeLead(){document.getElementById('leadModal').classList.remove('show');currentLeadId=null;}

function saveLead(){
  var lead = leads.find(function(l){return String(l.id)===String(currentLeadId);});
  if(!lead) return;
  lead.company = document.getElementById('lmCompany').value;
  lead.contact = document.getElementById('lmContact').value;
  lead.phone = document.getElementById('lmPhone').value;
  lead.email = document.getElementById('lmEmail').value;
  lead.shipments = parseInt(document.getElementById('lmShipments').value)||0;
  lead.type = document.getElementById('lmType').value;
  lead.source = document.getElementById('lmSource').value;
  lead.status = document.getElementById('lmStatus').value;
  lead.meetingDate = document.getElementById('lmMeetingDate').value||'';
  lead.meetingLink = document.getElementById('lmMeetingLink').value||'';
  lead.telegram = document.getElementById('lmTelegram').value||'';
  lead.telegramGroup = document.getElementById('lmTelegramGroup').value||'';

  var cmt = document.getElementById('lmNewComment').value.trim();
  if(cmt){if(!lead.comments) lead.comments=[];lead.comments.push({text:cmt, date:new Date().toLocaleString('uk-UA')});}

  apiPut(lead); saveLocal(); closeLead(); renderBoard();
}

function deleteLead(){
  if(!confirm('Видалити заявку?')) return;
  apiDelete(currentLeadId);
  leads = leads.filter(function(l){return String(l.id)!==String(currentLeadId);});
  saveLocal(); closeLead(); renderBoard();
}

/* ===== NEW LEAD ===== */
function openNewLead(){document.getElementById('newLeadModal').classList.add('show');['nlCompany','nlContact','nlPhone','nlEmail','nlShipments'].forEach(function(id){document.getElementById(id).value='';});}
function closeNewLead(){document.getElementById('newLeadModal').classList.remove('show');}
function saveNewLead(){
  var newLead = {company:document.getElementById('nlCompany').value,contact:document.getElementById('nlContact').value,phone:document.getElementById('nlPhone').value,email:document.getElementById('nlEmail').value,shipments:parseInt(document.getElementById('nlShipments').value)||0,type:document.getElementById('nlType').value,source:document.getElementById('nlSource').value,status:'new',date:new Date().toISOString().slice(0,10),comments:[],files:[],telegram:'',telegramGroup:'',meetingDate:'',meetingLink:''};
  apiPost(newLead).then(function(saved){if(saved&&saved.id)newLead.id=saved.id;else newLead.id=Date.now().toString();leads.push(newLead);saveLocal();closeNewLead();renderBoard();});
}

/* ===== CSV ===== */
function exportCSV(){var h='Компанія,Контакт,Телефон,Email,Telegram,Статус,Джерело,Дата\n';var rows=leads.map(function(l){return[l.company,l.contact,l.phone,l.email,l.telegram||'',l.status,l.source,l.date].map(function(v){v=String(v||'');return v.indexOf(',')>-1?'"'+v+'"':v;}).join(',');}).join('\n');var blob=new Blob(['\uFEFF'+h+rows],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='mtp-leads.csv';a.click();}

document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeLead();closeNewLead();}});

apiGet().then(function(){renderBoard();});
