import initDraftailEditor from './wagtaildraftail';

describe('wagtaildraftail', () => {
  it('exists', () => {
    expect(initDraftailEditor).toBeInstanceOf(Function);
  });

  it('is exposed as global', () => {
    expect(window.initDraftailEditor).toBe(initDraftailEditor);
  });

  it('initialises the editor', () => {
    document.body.innerHTML = `
      <div>
        <input type="text" name="test" value="null"/>
      </div>
    `;

    initDraftailEditor('test');
    expect(document.querySelector('.DraftEditor-root')).toBeDefined();
  });
});
