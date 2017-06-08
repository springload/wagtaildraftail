/**
 * Wagtail-related helpers for Nightmare tests
 */

const LOGIN_PATH = '/admin/login/';
const PAGE_PATH = '/admin/pages/';
const LOGIN_FORM = `[action="${LOGIN_PATH}"]`;

export const loginForm = (username, password) => {
  return (nightmare) => {
    nightmare
      .type(`${LOGIN_FORM} #id_username`, username)
      .type(`${LOGIN_FORM} #id_password`, password)
      .click(`${LOGIN_FORM} [type="submit"]`)
      .wait();
  };
};

export const login = (domain, username, password) => {
  return (nightmare) => {
    nightmare
      .cookies.clearAll()
      .goto(`http://${domain}${LOGIN_PATH}`)
      .use(loginForm(username, password));
  };
};

export const edit = (domain, pageId) => {
  return (nightmare) => {
    nightmare
      .goto(`http://${domain}${PAGE_PATH}${pageId}/edit/`);
  };
};
