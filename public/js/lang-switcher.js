(function() {
  var LANG_MAP = [
    ['/', '/ru/', '/en/'],
    ['/ua/about/', '/about/', '/en/about/'],
    ['/ua/blog/', '/blog/', '/en/blog/'],
    ['/ua/recalls/', '/recalls/', '/en/recalls/'],
    ['/ua/guide/', '/guide/', '/en/guide/'],
    ['/ua/calculator/', '/calculator/', '/en/calculator/'],
    ['/ua/3pl-logistyka/', '/ru/services/', '/en/services/'],
    ['/ua/fulfilment-vazhkykh-tovariv/', '/fulfilment-vazhkykh-tovariv/', '/en/heavy-goods/'],
    ['/ua/thanks/', '/thanks/', '/en/thanks/'],
    ['/ua/tsiny/', '/tsenu/', '/en/prices/'],
    ['/ua/fulfilment-dlya-internet-magazynu/', '/fulfilment-dlya-internet-magazynu/', null],
  ];

  var BLOG_MAP = [
    ['d0kknsayu1-fulfillment-chi-vlasnii-sklad-u-2025-str', 'pp8gsej3c1-fulfilment-protiv-sobstvennogo-sklada-v', 'fulfillment-vs-own-warehouse-2025'],
    ['gdf6pzul31-top-5-pomilok-yak-vbivayut-logstiku-nter', 'xh1rdimut1-5-glavnih-oshibok-v-logistike-internet-m', 'top-5-logistics-mistakes-ecommerce'],
    ['s7non1f0y1-scho-take-sla-v-logstits-chomu-tse-klyuc', 'pdjm77ogc1-chto-takoe-sla-v-logistike-i-pochemu-eto', 'what-is-sla-in-logistics'],
    ['bl9h476gp1-top-5-pomilok-u-logstits-pd-chas-sezonni', 'do95mhtv41-naibolee-chastie-oshibki-v-logistike-vo', 'peak-season-logistics-mistakes'],
    ['5vlhyoip61-chomu-lipen-chas-perevriti-vash-sklad-ch', 'fxaeldo931-pochemu-iyul-luchshee-vremya-proverit-v', 'why-audit-warehouse-in-summer'],
    ['699f3hz0v1-yak-pratsyu-fulflment-v-ukran-2025-ekspe', 'keantd63p1-kak-rabotaet-fulfilment-v-ukraine-2025-o', 'how-fulfillment-works-ukraine-2025'],
    ['2fz7njsgn1-scho-take-artikul-yak-pravilno-iogo-stvo', null, 'what-is-sku-article-number'],
    ['edt36a00r1-yakii-bznes-vdkriti-v-ukran-mozhlivost-d', '33bmy57t51-kakoi-biznes-otkrit-v-ukraine-vozmozhnos', 'best-business-ideas-ukraine'],
    ['k6e9sg89y1-yak-vdkriti-nternet-magazin-v-ukran-osno', 'yzhv774pa1-kak-otkrit-internet-magazin-v-ukraine-os', 'how-to-start-online-store-ukraine'],
    ['27jibr7e81-bznes-v-ukran-pd-chas-vini-vikliki-ta-mo', 'h4mk9ml261-biznes-v-ukraine-vo-vremya-voini-vizovi', 'business-in-ukraine-during-war'],
    ['iyjgnyrmx1-rro-prro-dlya-bznesu-osoblivost-ta-vimog', '60er8zh601-rro-i-prro-dlya-biznesa-osobennosti-i-tr', 'fiscal-register-prro-business'],
    ['xz8vfk1jg1-tovarnii-bznes-v-ukran-osoblivost-ta-per', '8emi42xu61-tovarnii-biznes-v-ukraine-osobennosti-i', 'product-business-ukraine-guide'],
    ['1uxlzxirt1-5-golovnih-pomilok-pd-chas-vdkrittya-nte', 'e3uzpiaja1-5-glavnih-oshibok-pri-otkritii-internet', '5-mistakes-starting-online-store'],
    ['jghdgatid1-yak-vdkriti-nternet-magazin-pd-chas-vini', 'okobnaenu1-kak-otkrit-internet-magazin-vo-vremya-vo', 'online-store-during-wartime'],
    ['1zah21gka1-chim-zamniti-rosisk-servsi-chek-list-dly', 'a5zlsrmfs1-chem-zamenit-rossiiskie-servisi-chek-lis', 'replace-russian-services-ukraine-checklist'],
    ['13ny6p72v1-yak-pdgotuvati-nternet-magazin-do-8-bere', 'ka4rkudet1-kak-podgotovit-internet-magazin-k-8-mart', 'prepare-online-store-march-8'],
    ['1z05mldbb1-yak-nternet-magazinu-pratsyuvati-z-vdguk', 'mjrp3rx3z1-kak-internet-magazinu-rabotat-s-otzivami', 'how-to-handle-customer-reviews'],
    ['53yjx8x051-yak-nternet-magazinu-zahistitisya-vd-sha', '1sn3nscy81-moshennichestvo-klientov-pri-pokupke-v-i', 'protect-store-from-fraud'],
    ['5kfyptimc1-10-robochih-sposobv-zblshiti-pributok-nt', 'iavfdk7371-10-rabochih-sposobov-uvelichit-pribil-in', '10-ways-increase-profit-ecommerce'],
    ['8mcui07l11-yak-skorotiti-klkst-povernen-tovaru-v-nt', 'o5x60a9nk1-kak-sokratit-kolichestvo-vozvratov-tovar', 'reduce-product-returns-ecommerce'],
    ['bgt5cmsix1-svi-sklad-vs-fulflment-scho-obrati-vlasn', '25m6cs3xd1-svoi-sklad-vs-fulfilment-chto-vibrat-vla', 'fulfillment-vs-own-warehouse'],
    ['elrpmubzt1-scho-potrbno-znati-pro-povednku-pokuptsv', '2b5uuyxzx1-chto-nuzhno-znat-o-povedenii-pokupatelei', 'online-buyer-behavior-insights'],
    ['hmh91dbl11-mtp-group-fulfillment-naikrasch-fulflmen', null, 'mtp-group-best-fulfillment-operators'],
    ['2lpu5l5sa1-mtp-group-dinii-v-ukran-servs-z-shvidko', null, 'mtp-group-fast-product-liquidation'],
    ['3tdig7x6z1-rro-dlya-nternet-magazinu-yak-vesti-bzne', 'n2a9117991-rro-dlya-internet-magazina-kak-vesti-biz', 'fiscal-register-requirements-ukraine'],
    ['l69lld8l41-scho-take-fulflment-dlya-nternet-magazin', 'm2l0va78z1-chto-takoe-fulfilment-dlya-internet-maga', 'what-is-fulfillment-7-services'],
    ['ldos1bvrh1-yak-pdgotuvati-nternet-magazin-do-novorc', 'im5rupthp1-kak-podgotovit-internet-magazin-k-novogo', 'prepare-store-for-holidays'],
    ['lgl2mu2gb1-yak-vibrati-fulflment-operatora-v-ukran', '2k76ljgp91-kak-vibrat-fulfilment-operatora-v-ukrain', 'how-to-choose-fulfillment-operator'],
    ['mj3ulhpr21-yak-nternet-magazinu-pratsyuvati-v-umova', 'tl4cc8e601-kak-internet-magazinu-rabotat-v-usloviya', 'ecommerce-logistics-during-war'],
    ['n2kn0z1f21-7-trendv-nternet-torgvl-u-2022-rots-scho', 'kahfgm2161-7-trendov-internet-torgovli-v-2022-godu', 'ecommerce-trends-2022'],
    ['psumj0frr1-dohd-a-pributku-nema-de-vtracha-grosh-nt', '6bcn9jn3b1-dohod-est-a-pribili-net-gde-teryaet-deng', 'where-online-store-loses-money'],
    ['rjmgtrmvb1-fulflment-scho-tse-sklki-koshtu-ta-nsh-v', 'jveoso2gb1-fulfilment-chto-eto-skolko-stoit-i-drugi', 'fulfillment-cost-guide'],
    ['uec3upu741-fulflment-dlya-nternet-magazinu-odyagu-t', 'ak35ism111-fulfilment-dlya-internet-magazina-odezhd', 'fulfillment-for-clothing-shoes'],
    ['vzfshz9ht1-yak-ukranskim-pdprimtsyam-viiti-na-vrope', '2l10ulx751-kak-ukrainskim-predprinimatelyam-viiti-n', 'expand-to-european-marketplaces'],
    ['zmck0cika1-yak-nternet-magazinu-pdgotuvatisya-do-dn', 'l7otgimlh1-kak-internet-magazinu-podgotovitsya-k-dn', 'prepare-store-valentines-day'],
  ];

  BLOG_MAP.forEach(function(row) {
    LANG_MAP.push([
      '/ua/blog/tpost/' + row[0] + '/',
      row[1] ? '/blog/tpost/' + row[1] + '/' : '/blog/',
      '/en/blog/post/' + row[2] + '/'
    ]);
  });

  var LOOKUP = {};
  LANG_MAP.forEach(function(row) {
    var ua = row[0], ru = row[1], en = row[2];
    var entry = { ua: ua, ru: ru, en: en };
    [ua, ru, en].forEach(function(p) {
      if (!p) return;
      LOOKUP[p] = entry;
      if (p.endsWith('/') && p.length > 1) LOOKUP[p.slice(0,-1)] = entry;
      if (!p.endsWith('/')) LOOKUP[p + '/'] = entry;
    });
  });

  function updateNavLinks() {
    var path = window.location.pathname;
    var entry = LOOKUP[path] || LOOKUP[path + '/'] || LOOKUP[path.replace(/\/$/, '')];
    if (!entry) return;
    var navRight = document.querySelector('.nav-right');
    if (!navRight) return;
    navRight.querySelectorAll('a[href]').forEach(function(a) {
      var h = a.getAttribute('href');
      if ((h === '/' || h === '/ua' || h === '/ua/') && entry.ua) a.href = entry.ua;
      if ((h === '/ru' || h === '/ru/') && entry.ru) a.href = entry.ru;
      if ((h === '/en' || h === '/en/') && entry.en) a.href = entry.en;
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', updateNavLinks);
  else updateNavLinks();
})();
