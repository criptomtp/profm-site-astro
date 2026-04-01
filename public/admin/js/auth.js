/* Simple Auth — works without API */
var USERS = {
  'mtp_admin': {password:'MTP2026secure!', name:'Адмін', role:'admin', permissions:['crm','dashboard','seo','content','settings','users']},
  'manager1': {password:'Manager2026!', name:'Дмитро', role:'manager', permissions:['crm','dashboard']}
};

function checkAuth(){
  if(sessionStorage.getItem('isAdmin')!=='true') window.location.href='/admin/';
}

function getUser(){
  try{return JSON.parse(sessionStorage.getItem('mtp_user')||'{}');}catch(e){return {};}
}

function handleLogin(e){
  e.preventDefault();
  var login=document.getElementById('login').value.trim();
  var pass=document.getElementById('password').value;
  var err=document.getElementById('loginError');

  var user=USERS[login];
  if(user && user.password===pass){
    sessionStorage.setItem('isAdmin','true');
    sessionStorage.setItem('mtp_user',JSON.stringify({name:user.name,role:user.role,permissions:user.permissions}));
    window.location.href='/admin/dashboard.html';
  } else {
    err.style.display='block';
    err.textContent='Невірний логін або пароль';
  }
}

function logout(){
  sessionStorage.clear();
  window.location.href='/admin/';
}
