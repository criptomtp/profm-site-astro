/* Auth — session-based via API */
var SESSION_KEY = 'mtp_session';
var USER_KEY = 'mtp_user';

function getSessionToken() {
  return localStorage.getItem(SESSION_KEY) || '';
}

function getUser() {
  try { return JSON.parse(localStorage.getItem(USER_KEY) || '{}'); } catch (e) { return {}; }
}

function hasPermission(p) {
  var u = getUser();
  if (!u.permissions) return false;
  return u.role === 'admin' || u.permissions.indexOf(p) !== -1;
}

function authHeaders() {
  return { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + getSessionToken() };
}

function authFetch(url, opts) {
  opts = opts || {};
  opts.headers = Object.assign({}, opts.headers || {}, { 'Authorization': 'Bearer ' + getSessionToken() });
  return fetch(url, opts);
}

function checkAuth() {
  var token = getSessionToken();
  if (!token) { window.location.href = '/admin/'; return; }

  fetch('/api/auth?action=check', { headers: { 'Authorization': 'Bearer ' + token } })
    .then(function (r) {
      if (!r.ok) throw new Error('expired');
      return r.json();
    })
    .then(function (d) {
      if (!d.ok) throw new Error('invalid');
      localStorage.setItem(USER_KEY, JSON.stringify(d.user));
    })
    .catch(function () {
      localStorage.removeItem(SESSION_KEY);
      localStorage.removeItem(USER_KEY);
      window.location.href = '/admin/';
    });
}

function handleLogin(e) {
  e.preventDefault();
  var login = document.getElementById('login').value.trim();
  var pass = document.getElementById('password').value;
  var err = document.getElementById('loginError');
  var btn = e.target.querySelector('button[type="submit"]');
  err.style.display = 'none';

  if (!login || !pass) {
    err.style.display = 'block';
    err.textContent = 'Введіть логін і пароль';
    return;
  }

  btn.disabled = true;
  btn.textContent = 'Вхід...';

  fetch('/api/auth', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ action: 'login', username: login, password: pass })
  })
    .then(function (r) { return r.json().then(function (d) { return { status: r.status, data: d }; }); })
    .then(function (res) {
      if (res.data.ok && res.data.session) {
        localStorage.setItem(SESSION_KEY, res.data.session);
        localStorage.setItem(USER_KEY, JSON.stringify(res.data.user || {}));
        window.location.href = '/admin/dashboard.html';
      } else {
        err.style.display = 'block';
        if (res.status === 429) {
          err.textContent = 'Забагато спроб. Спробуйте через хвилину.';
        } else {
          err.textContent = 'Невірний логін або пароль';
        }
      }
    })
    .catch(function () {
      err.style.display = 'block';
      err.textContent = 'Помилка з\'єднання з сервером';
    })
    .finally(function () {
      btn.disabled = false;
      btn.textContent = 'Увійти';
    });
}

function logout() {
  var token = getSessionToken();
  if (token) {
    fetch('/api/auth', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token },
      body: JSON.stringify({ action: 'logout' })
    }).catch(function () { });
  }
  localStorage.removeItem(SESSION_KEY);
  localStorage.removeItem(USER_KEY);
  window.location.href = '/admin/';
}
