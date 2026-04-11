/**
 * Universal FAQ accordion handler.
 * Supports all class-name variants used across the site:
 *   .faq-q / .faq-a / .faq-item
 *   .sb-faq-q / .sb-faq-a / .sb-faq-item
 *   .kv-faq-q / .kv-faq-a / .kv-faq-item
 *   .ky-faq-q / .ky-faq-a / .ky-faq-item
 *   .ek-faq-q / .ek-faq-a / .ek-faq-item
 *   .faq-question / .faq-answer / .faq-item
 */
(function(){
  var btnSel = '.faq-q,.sb-faq-q,.kv-faq-q,.ky-faq-q,.ek-faq-q,.faq-question';
  var ansSel = '.faq-a,.sb-faq-a,.kv-faq-a,.ky-faq-a,.ek-faq-a,.faq-answer';
  var openSel = '.faq-item.open,.sb-faq-item.open,.kv-faq-item.open,.ky-faq-item.open,.ek-faq-item.open';

  document.querySelectorAll(btnSel).forEach(function(btn){
    btn.addEventListener('click',function(){
      var item = btn.parentElement;
      var a = item.querySelector(ansSel);
      var isOpen = item.classList.contains('open');
      // Close all open items
      document.querySelectorAll(openSel).forEach(function(el){
        el.classList.remove('open');
        var content = el.querySelector(ansSel);
        if(content) content.style.maxHeight = null;
      });
      // Open clicked item if it was closed
      if(!isOpen){
        item.classList.add('open');
        if(a) a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });
})();
