import React from 'react';
import ReactDOM from 'react-dom';

import DraftailEditor, { ENTITY_TYPE } from 'draftail';

import 'draftail/dist/draftail.css';
import './wagtaildraftail.css';

import LinkSource from './sources/LinkSource';
import ImageSource from './sources/ImageSource';
import DocumentSource from './sources/DocumentSource';
import EmbedSource from './sources/EmbedSource';

import Link, { findLinkEntities } from './entities/Link';
import Document, { findDocumentEntities } from './entities/Document';

const controls = {};
controls[ENTITY_TYPE.IMAGE] = ImageSource;
controls[ENTITY_TYPE.EMBED] = EmbedSource;
controls[ENTITY_TYPE.LINK] = LinkSource;
controls[ENTITY_TYPE.DOCUMENT] = DocumentSource;

const strategies = {};
strategies[ENTITY_TYPE.LINK] = findLinkEntities;
strategies[ENTITY_TYPE.DOCUMENT] = findDocumentEntities;

const decorators = {};
decorators[ENTITY_TYPE.LINK] = Link;
decorators[ENTITY_TYPE.DOCUMENT] = Document;

const initDraftailEditor = (fieldName, options = {}) => {
  const field = document.querySelector(`[name="${fieldName}"]`);
  const editorWrapper = document.createElement('div');
  field.parentNode.appendChild(editorWrapper);

  const serialiseInputValue = (rawContentState) => {
    field.value = JSON.stringify(rawContentState);
  };

  if (options.entityTypes) {
    // eslint-disable-next-line no-param-reassign
    options.entityTypes = options.entityTypes.map(entity => Object.assign(entity, {
      control: controls[entity.type],
      strategy: strategies[entity.type],
      component: decorators[entity.type],
    }));
  }

  const editor = (
    <DraftailEditor
      rawContentState={JSON.parse(field.value)}
      onSave={serialiseInputValue}
      {...options}
    />
  );

  ReactDOM.render(editor, editorWrapper);
};

window.initDraftailEditor = initDraftailEditor;

export default initDraftailEditor;
