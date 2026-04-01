/* Auth — simple + API */
function checkAuth(){
  if(sessionStorage.getItem('isAdmin')!=='true') window.location.href='/admin/';
}
function getUser(){
  try{return JSON.parse(sessionStorage.getItem('mtp_user')||'{}');}catch(e){return {};}
}
function hasPermission(p){
  var u=getUser();if(!u.permissions)return true;return u.permissions.indexOf(p)!==-1;
}

function handleLogin(e){
  e.preventDefault();
  var login=document.getElementById('login').value.trim();
  var pass=document.getElementById('password').value;
  var err=document.getElementById('loginError');
  err.style.display='none';
  sessionStorage.clear();

  // Hardcoded users (always work, no API needed)
  var USERS={
    'mtp_admin':{password:'MTP2026secure!',name:'Адмін',role:'admin',permissions:['crm','dashboard','seo','content','settings','users']},
    'manager1':{password:'Manager2026!',name:'Дмитро',role:'manager',permissions:['crm','dashboard']}
  };

  // Try hardcoded first
  var u=USERS[login];
  if(u && u.password===pass){
    sessionStorage.setItem('isAdmin','true');
    sessionStorage.setItem('mtp_user',JSON.stringify({name:u.name,role:u.role,permissions:u.permissions}));
    window.location.href='/admin/dashboard.html';
    return;
  }

  // Try API for dynamic users
  fetch('/api/auth',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action:'login',username:login,password:pass})})
  .then(function(r){return r.json();})
  .then(function(d){
    if(d.ok){
      sessionStorage.setItem('isAdmin','true');
      sessionStorage.setItem('mtp_user',JSON.stringify(d.user||{}));
      window.location.href='/admin/dashboard.html';
    } else {
      err.style.display='block';
      err.textContent=d.error||'Невірний логін або пароль';
    }
  })
  .catch(function(){
    err.style.display='block';
    err.textContent='Невірний логін або пароль';
  });
}

function logout(){sessionStorage.clear();window.location.href='/admin/';}
