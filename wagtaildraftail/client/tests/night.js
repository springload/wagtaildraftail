/* eslint-disable no-console, import/no-extraneous-dependencies */
import nightmare from 'nightmare';

jasmine.DEFAULT_TIMEOUT_INTERVAL = 20000; // eslint-disable-line no-undef

const TEST_DOMAIN = process.env.TEST_DOMAIN || 'localhost:8000';

// Use a custom type function that fires an event React detects.
// See http://stackoverflow.com/questions/23892547/what-is-the-best-way-to-trigger-onchange-event-in-react-js
nightmare.action('type', function type(selector, text, done) {
  this.evaluate_now((sel, txt) => {
    const elem = document.querySelector(sel);
    elem.focus();
    elem.value = txt;
    elem.blur();
    elem.dispatchEvent(new Event('input', { bubbles: true }));
  }, done, selector, text);
});

nightmare.action('text', function text(selector, done) {
  this.evaluate_now((sel) => {
    const elt = document.querySelector(sel);
    return elt ? elt.textContent : null;
  }, done, selector);
});

nightmare.action('value', function value(selector, done) {
  this.evaluate_now((sel) => {
    const elt = document.querySelector(sel);
    return elt ? elt.value : null;
  }, done, selector);
});

nightmare.action('nbElements', function nbElements(selector, done) {
  this.evaluate_now((sel) => {
    const elt = document.querySelectorAll(sel);
    return elt ? elt.length : 0;
  }, done, selector);
});

const night = nightmare({
  show: true,
  width: 1024,
  height: 768,
  // titleBarStyle: 'hidden',
});

night.on('page', (type, message, additionalMessage) => {
  console.log(type, message, additionalMessage);
});

night.on('console', (type, message, additionalMessage) => {
  console.log(type, message, additionalMessage);
});

night.TEST_DOMAIN = TEST_DOMAIN;

export default night;
