/* bcom ICT — minimal progressive enhancement.
   Nothing on this site depends on JavaScript to render: AI crawlers largely
   don't execute JS, so all content ships in the HTML. This only handles the
   mobile nav toggle. */
(function () {
  var btn = document.querySelector('.navtoggle');
  var nav = document.getElementById('mobilenav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    nav.setAttribute('data-open', String(!open));
  });
})();
