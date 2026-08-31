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

/* Contact form — submit in place so the visitor never leaves the site.
   Progressive enhancement only: with JavaScript off the form still POSTs
   normally to Formspree, which is why the action and hidden fields stay in
   the HTML. Nothing here is required for the page to work. */
(function () {
  var form = document.querySelector('form.enquiry');
  if (!form || !window.fetch) return;

  var btn = form.querySelector('button[type="submit"]');
  var original = btn ? btn.textContent : '';

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    }).then(function (res) {
      return res.ok ? res.json() : Promise.reject(res);
    }).then(function () {
      var done = document.createElement('div');
      done.className = 'form-done';
      done.setAttribute('role', 'status');
      done.innerHTML =
        '<h3>Thanks — that\'s reached us</h3>' +
        '<p>We\'ll come back to you within 4 business hours, during business hours: ' +
        '8:00am to 5:00pm, Monday to Friday, Brisbane time.</p>' +
        '<p>If it\'s urgent, call <a href="tel:+61730418993"><strong>07 3041 8993</strong></a> ' +
        'rather than waiting on the email.</p>';
      form.replaceWith(done);
      done.focus && done.focus();
    }).catch(function () {
      if (btn) { btn.disabled = false; btn.textContent = original; }
      var err = form.querySelector('.form-error');
      if (!err) {
        err = document.createElement('p');
        err.className = 'form-error';
        err.setAttribute('role', 'alert');
        form.appendChild(err);
      }
      err.innerHTML = 'That didn\'t send. Please email ' +
        '<a href="mailto:support@bcomservices.com">support@bcomservices.com</a> or call ' +
        '<a href="tel:+61730418993">07 3041 8993</a> and we\'ll pick it up.';
    });
  });
})();
