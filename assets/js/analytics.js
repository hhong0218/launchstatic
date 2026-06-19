(function () {
  'use strict';

  var MEASUREMENT_ID = window.LS_GA_MEASUREMENT_ID || '';
  var CONSENT_KEY = 'ls-cookie-ok';
  var loaded = false;

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  gtag('consent', 'default', {
    analytics_storage: 'denied',
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    wait_for_update: 500
  });

  function isConfigured() {
    return MEASUREMENT_ID && MEASUREMENT_ID.indexOf('G-') === 0 && MEASUREMENT_ID.indexOf('XXXX') === -1;
  }

  function loadGoogleAnalytics() {
    if (loaded || !isConfigured()) return;
    loaded = true;

    gtag('consent', 'update', {
      analytics_storage: 'granted'
    });

    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(MEASUREMENT_ID);
    document.head.appendChild(script);

    gtag('js', new Date());
    gtag('config', MEASUREMENT_ID, {
      anonymize_ip: true,
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      send_page_view: true
    });
  }

  window.LS_loadAnalytics = loadGoogleAnalytics;

  if (localStorage.getItem(CONSENT_KEY) === '1') {
    loadGoogleAnalytics();
  }
})();