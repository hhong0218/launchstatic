(function () {
  'use strict';

  var toggle = document.querySelector('.menu-toggle');
  var mobileNav = document.querySelector('.nav-mobile');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var open = mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileNav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = document.getElementById('form-status');
      var name = contactForm.querySelector('[name="name"]').value.trim();
      var email = contactForm.querySelector('[name="email"]').value.trim();
      var subjectField = contactForm.querySelector('[name="subject"]');
      var subjectText = subjectField ? subjectField.value.trim() : '';
      var message = contactForm.querySelector('[name="message"]').value.trim();
      if (!name || !email || !message) {
        if (status) {
          status.textContent = 'Please fill in all required fields.';
          status.className = 'mt-2 text-muted';
        }
        return;
      }
      var subject = encodeURIComponent(subjectText || 'LaunchStatic contact from ' + name);
      var body = encodeURIComponent('Name: ' + name + '\nEmail: ' + email + (subjectText ? '\nSubject: ' + subjectText : '') + '\n\n' + message);
      window.location.href = 'mailto:hello@launchstatic.dev?subject=' + subject + '&body=' + body;
      if (status) {
        status.textContent = 'Opening your email client. If nothing opens, email hello@launchstatic.dev directly.';
        status.className = 'mt-2';
        status.style.color = 'var(--success)';
      }
    });
  }
  var cookieBanner = document.getElementById('cookie-banner');
  var cookieAccept = document.getElementById('cookie-accept');
  var gaConfigured = typeof window.LS_isGaConfigured === 'function' && window.LS_isGaConfigured();
  if (cookieBanner && !gaConfigured) {
    cookieBanner.hidden = true;
    cookieBanner.setAttribute('aria-hidden', 'true');
  } else if (cookieBanner && cookieAccept && !localStorage.getItem('ls-cookie-ok')) {
    cookieBanner.hidden = false;
    cookieAccept.addEventListener('click', function () {
      localStorage.setItem('ls-cookie-ok', '1');
      cookieBanner.hidden = true;
      if (typeof window.LS_loadAnalytics === 'function') {
        window.LS_loadAnalytics();
      }
    });
  }

  document.querySelectorAll('form[data-newsletter]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      var endpoint = form.getAttribute('data-endpoint') || '';
      if (endpoint.indexOf('YOUR_FORM_ID') !== -1) {
        e.preventDefault();
        var ok = form.querySelector('.newsletter-ok');
        if (ok) ok.hidden = false;
        form.querySelector('button[type=submit]').disabled = true;
      }
    });
  });
})();