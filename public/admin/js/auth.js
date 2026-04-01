/* Auth — API + hardcoded admin fallback */
var API = 'https://www.fulfillmentmtp.com.ua/api/auth';

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
  var btn=e.target.querySelector('button');
  err.style.display='none';
  if(btn) btn.textContent='Входимо...';
  sessionStorage.clear(); // Clear previous session

  fetch(API,{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({action:'login',username:login,password:pass})
  })
  .then(function(r){return r.json();})
  .then(function(data){
    if(data.ok){
      sessionStorage.setItem('isAdmin','true');
      sessionStorage.setItem('mtp_user',JSON.stringify(data.user||{}));
      window.location.href='/admin/dashboard.html';
    } else {
      err.style.display='block';
      err.textContent=data.error||'Невірний логін або пароль';
      if(btn) btn.textContent='Увійти';
    }
  })
  .catch(function(){
    // API failed — try hardcoded admin only
    if(login==='mtp_admin'&&pass==='MTP2026secure!'){
      sessionStorage.setItem('isAdmin','true');
      sessionStorage.setItem('mtp_user',JSON.stringify({name:'Адмін',role:'admin',permissions:['crm','dashboard','seo','content','settings','users']}));
      window.location.href='/admin/dashboard.html';
    } else {
      err.style.display='block';
      err.textContent='Помилка з\'єднання. Спробуйте ще раз.';
      if(btn) btn.textContent='Увійти';
    }
  });
}

function logout(){
  sessionStorage.clear();
  window.location.href='/admin/';
}
