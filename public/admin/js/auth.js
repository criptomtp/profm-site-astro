/* Auth with API + fallback to hardcoded */
var ADMIN_USER = 'mtp_admin';
var ADMIN_PASS = 'MTP2026secure!';

function getSession(){ return sessionStorage.getItem('mtp_session')||''; }
function getUser(){ try{return JSON.parse(sessionStorage.getItem('mtp_user')||'{}');}catch(e){return {};} }

function checkAuth() {
  if(!sessionStorage.getItem('isAdmin') && !getSession()){
    window.location.href = '/admin/';
  }
}

function hasPermission(perm){
  var user = getUser();
  if(!user.permissions) return true; // legacy admin
  return user.permissions.indexOf(perm) !== -1;
}

function handleLogin(e) {
  e.preventDefault();
  var login = document.getElementById('login').value;
  var pass = document.getElementById('password').value;
  var err = document.getElementById('loginError');

  // Try API first
  fetch('/api/auth?action=login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({action:'login', username:login, password:pass})
  }).then(function(r){return r.json();}).then(function(data){
    if(data.ok){
      sessionStorage.setItem('isAdmin', 'true');
      sessionStorage.setItem('mtp_session', data.session);
      sessionStorage.setItem('mtp_user', JSON.stringify(data.user));
      window.location.href = '/admin/dashboard.html';
    } else {
      err.style.display = 'block';
      err.textContent = data.error || 'Невірний логін або пароль';
    }
  }).catch(function(){
    // Fallback to hardcoded
    if(login === ADMIN_USER && pass === ADMIN_PASS){
      sessionStorage.setItem('isAdmin', 'true');
      sessionStorage.setItem('mtp_user', JSON.stringify({name:'Адмін',role:'admin',permissions:['crm','dashboard','seo','content','settings','users']}));
      window.location.href = '/admin/dashboard.html';
    } else {
      err.style.display = 'block';
      err.textContent = 'Невірний логін або пароль';
    }
  });
}

function logout() {
  sessionStorage.clear();
  window.location.href = '/admin/';
}
