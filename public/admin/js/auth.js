/* Auth with API + fallback */
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
  if(!user.permissions) return true;
  return user.permissions.indexOf(perm) !== -1;
}

function handleLogin(e) {
  e.preventDefault();
  var login = document.getElementById('login').value.trim();
  var pass = document.getElementById('password').value;
  var err = document.getElementById('loginError');
  err.style.display = 'none';

  // Try API
  fetch('/api/auth', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({action:'login', username:login, password:pass})
  }).then(function(r){
    if(!r.ok) throw new Error('API error '+r.status);
    return r.json();
  }).then(function(data){
    if(data.ok){
      sessionStorage.setItem('isAdmin', 'true');
      sessionStorage.setItem('mtp_session', data.session||'');
      sessionStorage.setItem('mtp_user', JSON.stringify(data.user||{}));
      window.location.href = '/admin/dashboard.html';
    } else {
      err.style.display = 'block';
      err.textContent = data.error || 'Невірний логін або пароль';
    }
  }).catch(function(e){
    console.log('API auth failed, trying fallback:', e.message);
    // Fallback to hardcoded admin
    if(login === ADMIN_USER && pass === ADMIN_PASS){
      sessionStorage.setItem('isAdmin', 'true');
      sessionStorage.setItem('mtp_user', JSON.stringify({name:'Адмін',role:'admin',permissions:['crm','dashboard','seo','content','settings','users']}));
      window.location.href = '/admin/dashboard.html';
    } else {
      err.style.display = 'block';
      err.textContent = 'Невірний логін або пароль (API недоступне — тільки адмін)';
    }
  });
}

function logout() {
  sessionStorage.clear();
  window.location.href = '/admin/';
}
