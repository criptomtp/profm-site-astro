var ARTICLES = [
  {title:'Fulfillment чи власний склад у 2025',date:'2025-08-10',lang:'UA',slug:'d0kknsayu1-fulfillment-chi-vlasnii-sklad-u-2025-str'},
  {title:'ТОП-5 помилок логістики інтернет-магазину',date:'2025-08-02',lang:'UA',slug:'gdf6pzul31-top-5-pomilok-yak-vbivayut-logstiku-nter'},
  {title:'SLA в логістиці: ключ до довіри клієнта',date:'2025-07-28',lang:'UA',slug:'s7non1f0y1-scho-take-sla-v-logstits-chomu-tse-klyuc'},
  {title:'П\'ять помилок логістики під час сезонних розпродажів',date:'2025-07-21',lang:'UA',slug:'bl9h476gp1-top-5-pomilok-u-logstits-pd-chas-sezonni'},
  {title:'Липень — ідеальний час для аудиту фулфілменту',date:'2025-07-01',lang:'UA',slug:'5vlhyoip61-chomu-lipen-chas-perevriti-vash-sklad-ch'},
  {title:'Як працює фулфілмент в Україні — 2025',date:'2025-06-17',lang:'UA',slug:'699f3hz0v1-yak-pratsyu-fulflment-v-ukran-2025-ekspe'},
  {title:'Що таке артикул: як правильно його створити',date:'2024-05-07',lang:'UA',slug:'2fz7njsgn1-scho-take-artikul-yak-pravilno-iogo-stvo'},
  {title:'Який бізнес відкрити в Україні',date:'2023-06-15',lang:'UA',slug:'edt36a00r1-yakii-bznes-vdkriti-v-ukran-mozhlivost-d'},
  {title:'Як відкрити інтернет-магазин в Україні',date:'2023-06-15',lang:'UA',slug:'k6e9sg89y1-yak-vdkriti-nternet-magazin-v-ukran-osno'},
  {title:'Бізнес в Україні під час війни',date:'2023-06-15',lang:'UA',slug:'27jibr7e81-bznes-v-ukran-pd-chas-vini-vikliki-ta-mo'},
  {title:'Товарний бізнес в Україні: особливості',date:'2023-06-15',lang:'UA',slug:'xz8vfk1jg1-tovarnii-bznes-v-ukran-osoblivost-ta-per'},
  {title:'РРО і пРРО для бізнесу',date:'2023-06-15',lang:'UA',slug:'iyjgnyrmx1-rro-prro-dlya-bznesu-osoblivost-ta-vimog'},
  {title:'5 головних помилок при відкритті інтернет-магазину',date:'2023-02-03',lang:'UA',slug:'1uxlzxirt1-5-golovnih-pomilok-pd-chas-vdkrittya-nte'},
  {title:'Як відкрити інтернет-магазин під час війни',date:'2022-07-02',lang:'UA',slug:'jghdgatid1-yak-vdkriti-nternet-magazin-pd-chas-vini'},
  {title:'Чим замінити російські сервіси: чек-лист',date:'2022-05-27',lang:'UA',slug:'1zah21gka1-chim-zamniti-rosisk-servsi-chek-list-dly'},
  {title:'Як вийти на європейські маркетплейси',date:'2022-04-24',lang:'UA',slug:'vzfshz9ht1-yak-ukranskim-pdprimtsyam-viiti-na-vrope'},
  {title:'Як працювати в умовах війни: логістика',date:'2022-04-01',lang:'UA',slug:'mj3ulhpr21-yak-nternet-magazinu-pratsyuvati-v-umova'},
  {title:'Як підготувати магазин до 8 березня',date:'2022-02-16',lang:'UA',slug:'13ny6p72v1-yak-pdgotuvati-nternet-magazin-do-8-bere'},
  {title:'Як працювати з відгуками',date:'2022-02-10',lang:'UA',slug:'1z05mldbb1-yak-nternet-magazinu-pratsyuvati-z-vdguk'},
  {title:'Фулфілмент: що це, скільки коштує',date:'2022-02-02',lang:'UA',slug:'rjmgtrmvb1-fulflment-scho-tse-sklki-koshtu-ta-nsh-v'},
  {title:'Шахрайство клієнтів при покупці',date:'2022-01-24',lang:'UA',slug:'53yjx8x051-yak-nternet-magazinu-zahistitisya-vd-sha'},
  {title:'Фулфілмент для одягу та взуття',date:'2022-01-21',lang:'UA',slug:'uec3upu741-fulflment-dlya-nternet-magazinu-odyagu-t'},
  {title:'Що таке фулфілмент: 7 основних послуг',date:'2022-01-20',lang:'UA',slug:'l69lld8l41-scho-take-fulflment-dlya-nternet-magazin'},
  {title:'Як підготуватися до Дня Валентина',date:'2022-01-17',lang:'UA',slug:'zmck0cika1-yak-nternet-magazinu-pdgotuvatisya-do-dn'},
  {title:'Дохід є, а прибутку немає',date:'2022-01-15',lang:'UA',slug:'psumj0frr1-dohd-a-pributku-nema-de-vtracha-grosh-nt'},
  {title:'Як скоротити повернення товару',date:'2022-01-14',lang:'UA',slug:'8mcui07l11-yak-skorotiti-klkst-povernen-tovaru-v-nt'},
  {title:'РРО для інтернет-магазину',date:'2022-01-14',lang:'UA',slug:'3tdig7x6z1-rro-dlya-nternet-magazinu-yak-vesti-bzne'},
  {title:'Як вибрати фулфілмент-оператора',date:'2022-01-14',lang:'UA',slug:'lgl2mu2gb1-yak-vibrati-fulflment-operatora-v-ukran'},
  {title:'Свій склад VS фулфілмент',date:'2022-01-13',lang:'UA',slug:'bgt5cmsix1-svi-sklad-vs-fulflment-scho-obrati-vlasn'},
  {title:'MTP GROUP — сервіс швидкої реалізації',date:'2022-01-13',lang:'UA',slug:'2lpu5l5sa1-mtp-group-dinii-v-ukran-servs-z-shvidko'},
  {title:'7 трендів інтернет-торгівлі 2022',date:'2022-01-03',lang:'UA',slug:'n2kn0z1f21-7-trendv-nternet-torgvl-u-2022-rots-scho'},
  {title:'Що потрібно знати про поведінку покупців',date:'2021-12-27',lang:'UA',slug:'elrpmubzt1-scho-potrbno-znati-pro-povednku-pokuptsv'},
  {title:'10 способів збільшити прибуток',date:'2021-12-21',lang:'UA',slug:'5kfyptimc1-10-robochih-sposobv-zblshiti-pributok-nt'},
  {title:'Як підготувати магазин до новорічних свят',date:'2021-12-13',lang:'UA',slug:'ldos1bvrh1-yak-pdgotuvati-nternet-magazin-do-novorc'},
  {title:'MTP Group Fulfillment — найкращі оператори',date:'2021-12-01',lang:'UA',slug:'hmh91dbl11-mtp-group-fulfillment-naikrasch-fulflmen'}
];

function renderArticles() {
  var tbody = document.getElementById('articlesBody');
  if (!tbody) return;
  tbody.innerHTML = ARTICLES.map(function(a) {
    var d = new Date(a.date);
    var dateStr = d.toLocaleDateString('uk-UA');
    return '<tr>' +
      '<td><strong>' + a.title + '</strong></td>' +
      '<td class="num">' + dateStr + '</td>' +
      '<td>' + a.lang + '</td>' +
      '<td>' +
        '<a href="/ua/blog/tpost/' + a.slug + '" target="_blank" class="btn btn-outline btn-sm">Переглянути</a>' +
      '</td>' +
      '</tr>';
  }).join('');
}

function slugify(text) {
  return text.toLowerCase()
    .replace(/[єї]/g,'i').replace(/і/g,'i').replace(/ґ/g,'g')
    .replace(/[ьъ]/g,'').replace(/я/g,'ya').replace(/ю/g,'yu')
    .replace(/ч/g,'ch').replace(/ш/g,'sh').replace(/щ/g,'shch')
    .replace(/ж/g,'zh').replace(/ц/g,'ts').replace(/х/g,'kh')
    .replace(/а/g,'a').replace(/б/g,'b').replace(/в/g,'v')
    .replace(/г/g,'h').replace(/д/g,'d').replace(/е/g,'e')
    .replace(/з/g,'z').replace(/и/g,'y').replace(/й/g,'i')
    .replace(/к/g,'k').replace(/л/g,'l').replace(/м/g,'m')
    .replace(/н/g,'n').replace(/о/g,'o').replace(/п/g,'p')
    .replace(/р/g,'r').replace(/с/g,'s').replace(/т/g,'t')
    .replace(/у/g,'u').replace(/ф/g,'f')
    .replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')
    .substring(0, 60);
}

function initNewArticle() {
  var titleInput = document.getElementById('articleTitle');
  var slugInput = document.getElementById('articleSlug');
  var descInput = document.getElementById('articleDesc');
  var charCount = document.getElementById('charCount');

  if (titleInput && slugInput) {
    titleInput.addEventListener('input', function() {
      slugInput.value = slugify(titleInput.value);
    });
  }
  if (descInput && charCount) {
    descInput.addEventListener('input', function() {
      var len = descInput.value.length;
      charCount.textContent = len + '/155';
      charCount.style.color = len > 155 ? '#e63329' : '#888';
    });
  }
}

function publishArticle(e) {
  e.preventDefault();
  var slug = document.getElementById('articleSlug').value;
  var lang = document.getElementById('articleLang').value;
  var prefix = lang === 'UA' ? '/ua' : '';
  var modal = document.getElementById('publishModal');
  var pathEl = document.getElementById('publishPath');
  if (pathEl) pathEl.textContent = 'public' + prefix + '/blog/tpost/' + slug + '/index.html';
  if (modal) modal.classList.add('show');
}

function closeModal() {
  var modal = document.getElementById('publishModal');
  if (modal) modal.classList.remove('show');
}
