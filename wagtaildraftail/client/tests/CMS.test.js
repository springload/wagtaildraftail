import night from './night';
import * as wagtail from './wagtail-night';

// TODO Skipped for now because those tests fail with test coverage measurement.
describe.skip('CMS', () => {
  describe('Login', () => {
    beforeAll(() => {
      return night.use(wagtail.login(night.TEST_DOMAIN, 'admin', 'admin')).wait(1000);
    });

    it('arrives on dashboard', async () => {
      expect(await night.exists('#wagtail.homepage')).toBe(true);
    });
  });

  describe('Edit', () => {
    beforeAll(() => {
      return night.use(wagtail.edit(night.TEST_DOMAIN, 3)).wait(1000);
    });

    it('has Draftail', async () => {
      expect(await night.exists('.DraftEditor-root')).toBe(true);
    });
  });

  describe('Logout', () => {
    beforeAll(() => {
      return night.click('[href="/admin/logout/"]').wait();
    });

    it('arrives with success message', async () => {
      expect(await night.text('.success')).toBe('You have been successfully logged out.');
    });
  });

  // TODO Should be an afterAll, but can't get it to work.
  afterAll(() => {
    return night.end();
  });
});
