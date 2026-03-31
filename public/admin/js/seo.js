// SEO baseline data — 23.03.2026
var SEO_BASELINE = {
  date: '2026-03-23',
  queries: [
    {q:'mtp group',clicks:51,impressions:99,ctr:51.5,position:2.3},
    {q:'фулфилмент',clicks:10,impressions:2741,ctr:0.4,position:9.8},
    {q:'фулфілмент україна',clicks:9,impressions:42,ctr:21.4,position:8.0},
    {q:'фулфілмент',clicks:8,impressions:1233,ctr:0.6,position:17.9},
    {q:'фулфилмент киев',clicks:6,impressions:171,ctr:3.5,position:2.7},
    {q:'артикул',clicks:4,impressions:3060,ctr:0.1,position:4.3},
    {q:'фулфілмент склад',clicks:2,impressions:55,ctr:3.6,position:4.6},
    {q:'фулфілмент для інтернет магазинів',clicks:2,impressions:37,ctr:5.4,position:26.5},
    {q:'що таке артикул',clicks:1,impressions:462,ctr:0.2,position:2.6},
    {q:'товарний бізнес це',clicks:1,impressions:375,ctr:0.3,position:9.0},
    {q:'mtp group fulfillment',clicks:1,impressions:18,ctr:5.6,position:1.2},
    {q:'фулфілмент послуги',clicks:1,impressions:89,ctr:1.1,position:12.4},
    {q:'склад фулфілмент київ',clicks:1,impressions:44,ctr:2.3,position:5.1},
    {q:'3pl оператор україна',clicks:0,impressions:31,ctr:0,position:18.7},
    {q:'фулфілмент бориспіль',clicks:0,impressions:12,ctr:0,position:3.2},
    {q:'фулфілмент ціна',clicks:0,impressions:67,ctr:0,position:22.1},
    {q:'що таке фулфілмент',clicks:0,impressions:245,ctr:0,position:14.3},
    {q:'фулфілмент для маркетплейсів',clicks:0,impressions:28,ctr:0,position:31.5},
    {q:'логістика для інтернет магазину',clicks:0,impressions:53,ctr:0,position:19.8},
    {q:'аутсорсинг логістики',clicks:0,impressions:41,ctr:0,position:25.3}
  ]
};

var TARGET_PAGES = [
  {url:'/ua/fulfilment-vazhkykh-tovariv',status:'pending',priority:'high',label:'Фулфілмент важких товарів'},
  {url:'/ua/tsiny',status:'pending',priority:'high',label:'Ціни на фулфілмент'},
  {url:'/ua/3pl-boryspil',status:'pending',priority:'medium',label:'3PL Бориспіль'},
  {url:'/ua/fulfilment-dlya-internet-magazinu',status:'pending',priority:'medium',label:'Фулфілмент для інтернет-магазину'},
  {url:'/ua/fulfilment-dlya-marketpleysiv',status:'pending',priority:'medium',label:'Фулфілмент для маркетплейсів'}
];

function initSeoChart() {
  var ctx = document.getElementById('posChart');
  if (!ctx) return;

  var top5 = SEO_BASELINE.queries.slice(0, 5);
  var colors = ['#e63329','#000','#666','#2196f3','#4caf50'];

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['23.03'],
      datasets: top5.map(function(q, i) {
        return {
          label: q.q,
          data: [q.position],
          borderColor: colors[i],
          backgroundColor: colors[i] + '20',
          borderWidth: 2,
          pointRadius: 5,
          tension: 0.3
        };
      })
    },
    options: {
      responsive: true,
      scales: {
        y: {
          reverse: true,
          min: 0,
          max: 30,
          title: { display: true, text: 'Позиція' }
        },
        x: {
          title: { display: true, text: 'Дата' }
        }
      },
      plugins: {
        legend: { position: 'bottom' }
      }
    }
  });
}

function renderSeoTable(page) {
  var perPage = 20;
  page = page || 1;
  var start = (page - 1) * perPage;
  var items = SEO_BASELINE.queries.slice(start, start + perPage);
  var tbody = document.getElementById('seoTableBody');
  if (!tbody) return;

  tbody.innerHTML = items.map(function(q, i) {
    return '<tr>' +
      '<td>' + q.q + '</td>' +
      '<td class="num">' + q.clicks + '</td>' +
      '<td class="num">' + q.impressions.toLocaleString() + '</td>' +
      '<td class="num">' + q.ctr.toFixed(1) + '%</td>' +
      '<td class="num">' + q.position.toFixed(1) + '</td>' +
      '<td>--</td>' +
      '</tr>';
  }).join('');
}
