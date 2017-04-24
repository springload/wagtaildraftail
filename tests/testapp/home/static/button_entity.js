const ButtonDecorator = ({ entityKey, children }) => {
  const attrs = {'data-tooltip': entityKey, className: 'RichEditor-button'};
  return window.wagtaildraftail.createElement('span', attrs, children);
};

window.wagtaildraftail.registerDecorator('ButtonDecorator', ButtonDecorator);
