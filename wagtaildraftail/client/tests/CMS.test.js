import night from './night';
import * as wagtail from './wagtail-night';

describe.skip('CMS', () => {
  describe('Login', () => {
    it('works', async () => {
      await night.use(wagtail.login(night.TEST_DOMAIN, 'admin', 'admin')).wait(1000);
      expect(await night.path()).toBe('/admin/');
    });

    it('arrives on dashboard', async () => {
      expect(await night.exists('#wagtail.homepage')).toBe(true);
    });
  });

  describe('Edit', () => {
    it('works', async () => {
      await night.use(wagtail.edit(night.TEST_DOMAIN, 3)).wait(1000);
      expect(await night.path()).toContain('/edit/');
    });

    it('has Draftail', async () => {
      expect(await night.exists('.DraftEditor-root')).toBe(true);
    });
  });

  describe('Logout', () => {
    it('works', async () => {
      await night.click('[href="/admin/logout/"]').wait();
      expect(await night.path()).toBe('/admin/login/');
    });

    it('arrives with success message', async () => {
      expect(await night.text('.success')).toBe('You have been successfully logged out.');
    });
  });

  // TODO Should be an afterAll, but can't get it to work.
  it('teardown nightmare instance', async () => {
    await night.end();
  });
});
