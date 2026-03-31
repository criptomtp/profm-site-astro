// Simple auth
var ADMIN_USER = 'mtp_admin';
var ADMIN_PASS = 'MTP2026secure!';

function checkAuth() {
  if (sessionStorage.getItem('isAdmin') !== 'true') {
    window.location.href = '/admin/';
  }
}

function handleLogin(e) {
  e.preventDefault();
  var login = document.getElementById('login').value;
  var pass = document.getElementById('password').value;
  var err = document.getElementById('loginError');
  if (login === ADMIN_USER && pass === ADMIN_PASS) {
    sessionStorage.setItem('isAdmin', 'true');
    window.location.href = '/admin/dashboard.html';
  } else {
    err.style.display = 'block';
    err.textContent = 'Невірний логін або пароль';
  }
}

function logout() {
  sessionStorage.removeItem('isAdmin');
  window.location.href = '/admin/';
}
