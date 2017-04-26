const ButtonDecorator = ({ entityKey, children }) => {
  const attrs = {'data-tooltip': entityKey, className: 'RichEditor-button'};
  return window.wagtailDraftail.createElement('span', attrs, children);
};

window.wagtailDraftail.registerDecorators({ ButtonDecorator });
