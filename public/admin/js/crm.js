/* ========== CRM v3 — MTP Group (Redis API) ========== */

var STATUSES = [
  {id:'new',label:'Нові',color:'#2196f3'},
  {id:'contact',label:'Контакт',color:'#ff9800'},
  {id:'negotiations',label:'Переговори',color:'#9c27b0'},
  {id:'onboarding',label:'Онбординг',color:'#4caf50'},
  {id:'clients',label:'Клієнти',color:'#000'}
];

var ONBOARDING_STEPS = [
  'Договір підписано','Товар прийнято на склад','Інтеграція CRM налаштована',
  'Тестове відправлення','Навчання менеджера','Перший робочий день','Перший тиждень — все ОК'
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
    // Fallback to localStorage
    var d = localStorage.getItem('mtp_crm_leads');
    if(d) leads = JSON.parse(d);
    return leads;
  });
}

function apiPost(lead){
  return fetch('/api/leads',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(lead)}).then(function(r){return r.json();}).catch(function(){return lead;});
}

function apiPut(lead){
  return fetch('/api/leads',{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify(lead)}).catch(function(){});
}

function apiDelete(id){
  return fetch('/api/leads?id='+id,{method:'DELETE'}).catch(function(){});
}

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
      return '<div class="kanban-card" data-id="'+l.id+'">' +
        '<div class="kc-company">'+(l.company||l.phone||'Без назви')+'</div>' +
        '<div class="kc-contact">'+(l.contact||'')+'</div>' +
        '<div class="kc-meta">'+(l.phone||'')+'</div>' +
        '</div>';
    }).join('');
  });

  // Add click handlers
  document.querySelectorAll('.kanban-card').forEach(function(card){
    card.addEventListener('click', function(){
      var id = card.getAttribute('data-id');
      openLead(id);
    });
  });

  renderStats();
}

function renderStats(){
  var el = document.getElementById('crmStats');
  if(!el) return;
  var total = leads.length;
  var newC = leads.filter(function(l){return l.status==='new';}).length;
  var clients = leads.filter(function(l){return l.status==='clients';}).length;
  el.innerHTML =
    '<div class="card"><div class="card-value">'+total+'</div><div class="card-label">Всього</div></div>' +
    '<div class="card"><div class="card-value">'+newC+'</div><div class="card-label">Нових</div></div>' +
    '<div class="card"><div class="card-value">'+clients+'</div><div class="card-label">Клієнтів</div></div>';
}

/* ===== LEAD MODAL ===== */
function openLead(id){
  var lead = leads.find(function(l){return String(l.id)===String(id);});
  if(!lead){alert('Лід не знайдений: '+id);return;}
  currentLeadId = id;

  var m = document.getElementById('leadModal');
  document.getElementById('lmTitle').textContent = lead.company || lead.phone || 'Заявка';
  document.getElementById('lmCompany').value = lead.company || '';
  document.getElementById('lmContact').value = lead.contact || '';
  document.getElementById('lmPhone').value = lead.phone || '';
  document.getElementById('lmEmail').value = lead.email || '';
  document.getElementById('lmShipments').value = lead.shipments || 0;
  document.getElementById('lmType').value = lead.type || 'other';
  document.getElementById('lmSource').value = lead.source || 'site';
  document.getElementById('lmStatus').value = lead.status || 'new';

  // Comments
  var cmDiv = document.getElementById('lmComments');
  var comments = lead.comments || [];
  cmDiv.innerHTML = comments.length ? comments.map(function(c){
    return '<div class="comment"><div class="comment-date">'+(c.date||'')+'</div><div class="comment-text">'+(c.text||'')+'</div></div>';
  }).join('') : '<p style="color:#888">Немає коментарів</p>';

  document.getElementById('lmNewComment').value = '';
  m.classList.add('show');
}

function closeLead(){
  document.getElementById('leadModal').classList.remove('show');
  currentLeadId = null;
}

function saveLead(){
  var lead = leads.find(function(l){return String(l.id)===String(currentLeadId);});
  if(!lead) return;

  lead.company = document.getElementById('lmCompany').value;
  lead.contact = document.getElementById('lmContact').value;
  lead.phone = document.getElementById('lmPhone').value;
  lead.email = document.getElementById('lmEmail').value;
  lead.shipments = parseInt(document.getElementById('lmShipments').value) || 0;
  lead.type = document.getElementById('lmType').value;
  lead.source = document.getElementById('lmSource').value;
  lead.status = document.getElementById('lmStatus').value;

  var cmt = document.getElementById('lmNewComment').value.trim();
  if(cmt){
    if(!lead.comments) lead.comments = [];
    lead.comments.push({text:cmt, date:new Date().toLocaleString('uk-UA')});
  }

  apiPut(lead);
  saveLocal();
  closeLead();
  renderBoard();
}

function deleteLead(){
  if(!confirm('Видалити заявку?')) return;
  apiDelete(currentLeadId);
  leads = leads.filter(function(l){return String(l.id)!==String(currentLeadId);});
  saveLocal();
  closeLead();
  renderBoard();
}

/* ===== NEW LEAD ===== */
function openNewLead(){
  document.getElementById('newLeadModal').classList.add('show');
  ['nlCompany','nlContact','nlPhone','nlEmail','nlShipments'].forEach(function(id){
    document.getElementById(id).value = '';
  });
}

function closeNewLead(){document.getElementById('newLeadModal').classList.remove('show');}

function saveNewLead(){
  var newLead = {
    company: document.getElementById('nlCompany').value,
    contact: document.getElementById('nlContact').value,
    phone: document.getElementById('nlPhone').value,
    email: document.getElementById('nlEmail').value,
    shipments: parseInt(document.getElementById('nlShipments').value) || 0,
    type: document.getElementById('nlType').value,
    source: document.getElementById('nlSource').value,
    status: 'new',
    date: new Date().toISOString().slice(0,10),
    comments: [],
    onboarding: [false,false,false,false,false,false,false]
  };

  apiPost(newLead).then(function(saved){
    if(saved && saved.id) newLead.id = saved.id;
    else newLead.id = Date.now().toString();
    leads.push(newLead);
    saveLocal();
    closeNewLead();
    renderBoard();
  });
}

/* ===== CSV EXPORT ===== */
function exportCSV(){
  var header = 'Компанія,Контакт,Телефон,Email,Статус,Джерело,Дата\n';
  var rows = leads.map(function(l){
    return [l.company,l.contact,l.phone,l.email,l.status,l.source,l.date].map(function(v){
      v = String(v||'');
      return v.indexOf(',')>-1 ? '"'+v+'"' : v;
    }).join(',');
  }).join('\n');
  var blob = new Blob(['\uFEFF'+header+rows],{type:'text/csv'});
  var a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'mtp-leads.csv';
  a.click();
}

/* ===== KEYBOARD ===== */
document.addEventListener('keydown',function(e){
  if(e.key==='Escape'){closeLead();closeNewLead();}
});

/* ===== INIT ===== */
apiGet().then(function(){renderBoard();});
