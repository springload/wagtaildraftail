import night from './night';

describe.skip('Homepage', () => {
  beforeAll(() => {
    return night.goto(`http://${night.TEST_DOMAIN}/`);
  });

  it('title', async () => {
    expect(await night.title()).toContain('wagtaildraftail');
  });

  it('renders', async () => {
    expect(await night.visible('[data-editor-draftail] iframe')).toEqual(true);
  });
});
