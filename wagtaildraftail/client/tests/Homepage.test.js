import night from './night';

describe.skip('Homepage', () => {
  it('works', async () => {
    await night.goto(`http://${night.TEST_DOMAIN}/`);
    expect(await night.path()).toEqual('/');
  });

  it('title', async () => {
    expect(await night.title()).toContain('wagtaildraftail');
  });

  it('renders', async () => {
    expect(await night.visible('[data-editor-draftail] iframe')).toEqual(true);
  });
});
