import initDraftailEditor from './wagtaildraftail';

describe('wagtaildraftail', () => {
  it('exists', () => {
    expect(initDraftailEditor).toBeInstanceOf(Function);
  });

  it('is exposed as global', () => {
    expect(window.initDraftailEditor).toBe(initDraftailEditor);
  });
});
