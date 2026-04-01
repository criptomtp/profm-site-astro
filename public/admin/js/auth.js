/* Auth */
function getSession(){ return sessionStorage.getItem('mtp_session')||''; }
function getUser(){ try{return JSON.parse(sessionStorage.getItem('mtp_user')||'{}');}catch(e){return {};} }

function checkAuth() {
  if(!sessionStorage.getItem('isAdmin')) window.location.href = '/admin/';
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
  var btn = e.target.querySelector('button[type="submit"]');
  err.style.display = 'none';
  if(btn) btn.textContent = 'Входимо...';

  // Always use www to avoid 307 redirect
  var apiUrl = 'https://www.fulfillmentmtp.com.ua/api/auth';
  // If on localhost, use relative
  if(location.hostname === 'localhost' || location.hostname === '127.0.0.1') apiUrl = '/api/auth';

  fetch(apiUrl, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({action:'login', username:login, password:pass})
  }).then(function(r){return r.json();}).then(function(data){
    if(data.ok){
      sessionStorage.setItem('isAdmin', 'true');
      sessionStorage.setItem('mtp_session', data.session||'');
      sessionStorage.setItem('mtp_user', JSON.stringify(data.user||{}));
      window.location.href = '/admin/dashboard.html';
    } else {
      err.style.display = 'block';
      err.textContent = data.error || 'Невірний логін або пароль';
      if(btn) btn.textContent = 'Увійти';
    }
  }).catch(function(e){
    console.error('Auth error:', e);
    // Fallback: hardcoded admin only
    if(login === 'mtp_admin' && pass === 'MTP2026secure!'){
      sessionStorage.setItem('isAdmin', 'true');
      sessionStorage.setItem('mtp_user', JSON.stringify({name:'Адмін',role:'admin',permissions:['crm','dashboard','seo','content','settings','users']}));
      window.location.href = '/admin/dashboard.html';
    } else {
      err.style.display = 'block';
      err.textContent = 'Помилка з\'єднання. Спробуйте ще раз.';
      if(btn) btn.textContent = 'Увійти';
    }
  });
}

function logout() {
  sessionStorage.clear();
  window.location.href = '/admin/';
}
