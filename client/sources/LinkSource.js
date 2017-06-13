import React from 'react';
import PropTypes from 'prop-types';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunkMiddleware from 'redux-thunk';

import { RichUtils } from 'draft-js';

import PageChooser from '../choosers/page/PageChooser';
import reducer from '../choosers/page/reducer';

// Plaster over Wagtail internals.
const buildInitialUrl = (entity, openAtParentId, canChooseRoot, pageTypes) => {
  // We can't destructure from the window object yet
  const pageChooser = global.chooserUrls.pageChooser;
  const emailLinkChooser = global.chooserUrls.emailLinkChooser;
  const externalLinkChooser = global.chooserUrls.externalLinkChooser;
  let url = pageChooser;

  if (openAtParentId) {
    url = `${url}${openAtParentId}/`;
  }

  const urlParams = {
    page_type: pageTypes.join(','),
    allow_external_link: true,
    allow_email_link: true,
    can_choose_root: canChooseRoot ? 'true' : 'false',
    link_text: '',
  };

  if (entity) {
    let data = entity.getData();

    if (typeof data === 'string') {
      data = { url: data, linkType: 'external', title: '' };
    }

    urlParams.link_text = data.title;

    switch (data.linkType) {
    case 'page':
      url = ` ${pageChooser}${data.parentId}/`;
      break;

    case 'email':
      url = emailLinkChooser;
      urlParams.link_url = data.url.replace('mailto:', '');
      break;

    default:
      url = externalLinkChooser;
      urlParams.link_url = data.url;
      break;
    }
  }

  return { url, urlParams };
};

const parsePageData = (pageData) => {
  const data = Object.assign({}, pageData);

  if (data.id) {
    data.linkType = 'page';
  } else if (data.url.indexOf('mailto:') === 0) {
    data.linkType = 'email';
  } else {
    data.linkType = 'external';
  }

  // We do not want each link to have the page's title as an attr.
  // nor links to have the link URL as a title.
  if (data.linkType === 'page' || data.url.replace('mailto:', '') === data.title) {
    delete data.title;
  }

  return data;
};

const middleware = [
  thunkMiddleware,
];

const store = createStore(reducer, {}, compose(
  applyMiddleware(...middleware),
  // Expose store to Redux DevTools extension.
  window.devToolsExtension ? window.devToolsExtension() : f => f
));

class LinkSource extends React.Component {
  constructor(props) {
    super(props);
    this.onClose = this.onClose.bind(this);
    this.onConfirm = this.onConfirm.bind(this);
  }

  componentDidMount() {
    const { entity } = this.props;
    const openAtParentId = false;
    const canChooseRoot = false;
    const pageTypes = ['wagtailcore.page'];
    const { url, urlParams } = buildInitialUrl(entity, openAtParentId, canChooseRoot, pageTypes);

    // $(document.body).on('hidden.bs.modal', this.onClose);

    // global.ModalWorkflow({
    //   url,
    //   urlParams,
    //   responses: {
    //     pageChosen: this.parseData,
    //   },
    // });
    // const modalPlacement = document.createElement('div');
    // modalPlacement.id = 'react-modal';
    // document.body.appendChild(modalPlacement);

    // const chooseButton = document.createElement('div');
    // chooseButton.className = 'action-choose';
    // document.body.appendChild(chooseButton);
    // window.createPageChooser(this.onConfirm);
  }

  componentWillUnmount() {

  }

  onConfirm(pageData) {
    const { editorState, options, onUpdate } = this.props;
    const data = parsePageData(pageData);
    const contentState = editorState.getCurrentContent();
    const contentStateWithEntity = contentState.createEntity(options.type, 'MUTABLE', data);
    const entityKey = contentStateWithEntity.getLastCreatedEntityKey();
    const nextState = RichUtils.toggleLink(editorState, editorState.getSelection(), entityKey);

    onUpdate(nextState);
  }

  onClose(e) {
    const { onClose } = this.props;
    e.preventDefault();

    onClose();
  }

  render() {
    return (
      <Provider store={store}>
        <PageChooser
          onModalClose={this.onClose}
          onPageChosen={this.onConfirm}
          initialParentPageId={null}
          restrictPageTypes={null}
        />
      </Provider>
    );
  }
}

LinkSource.propTypes = {
  editorState: PropTypes.object.isRequired,
  options: PropTypes.object.isRequired,
  // eslint-disable-next-line
  entity: PropTypes.object,
  onUpdate: PropTypes.func.isRequired,
  onClose: PropTypes.func.isRequired,
};

LinkSource.defaultProps = {
  entity: null,
};

export default LinkSource;
