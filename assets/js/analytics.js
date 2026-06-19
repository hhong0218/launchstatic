(function () {
  'use strict';

  var GA_ID = window.LS_GA_MEASUREMENT_ID || '';
  var CF_TOKEN = window.LS_CF_WEB_ANALYTICS_TOKEN || '';
  var CONSENT_KEY = 'ls-cookie-ok';
  var gaLoaded = false;
  var cfLoaded = false;

  function isGaConfigured() {
    return GA_ID && GA_ID.indexOf('G-') === 0 && GA_ID.indexOf('XXXX') === -1;
  }

  function isCfConfigured() {
    return CF_TOKEN && CF_TOKEN.indexOf('XXXX') === -1 && CF_TOKEN !== 'enable';
  }

  window.LS_isGaConfigured = isGaConfigured;

  function loadCloudflareWebAnalytics() {
    if (cfLoaded || !isCfConfigured()) return;
    cfLoaded = true;

    var script = document.createElement('script');
    script.defer = true;
    script.src = 'https://static.cloudflareinsights.com/beacon.min.js';
    script.setAttribute('data-cf-beacon', JSON.stringify({ token: CF_TOKEN }));
    document.head.appendChild(script);
  }

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

  function loadGoogleAnalytics() {
    if (gaLoaded || !isGaConfigured()) return;
    gaLoaded = true;

    gtag('consent', 'update', {
      analytics_storage: 'granted'
    });

    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(script);

    gtag('js', new Date());
    gtag('config', GA_ID, {
      anonymize_ip: true,
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      send_page_view: true
    });
  }

  window.LS_loadAnalytics = loadGoogleAnalytics;

  loadCloudflareWebAnalytics();

  if (localStorage.getItem(CONSENT_KEY) === '1') {
    loadGoogleAnalytics();
  }
})();