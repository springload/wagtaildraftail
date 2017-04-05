import React from 'react';
import ReactDOM from 'react-dom';
import { Entity } from 'draft-js';
import DraftailEditor from 'draftail';

import 'draftail/dist/draftail.css';
import './wagtaildraftail.css';

import sources from './sources';
import decorators from './decorators';

// TODO: Use the one from draftail once implemented https://github.com/springload/draftail/issues/48
const getEntityStrategy = (entityType) => {
    return (contentBlock, callback) => {
        contentBlock.findEntityRanges((character) => {
            const entityKey = character.getEntity();
            return (
                entityKey !== null &&
                Entity.get(entityKey).getType() === entityType
            );
        }, callback);
    };
};

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
      // TODO: Rename keys accordingly once changed in draftail https://github.com/springload/draftail/issues/49
      control: sources[entity.source],
      strategy: getEntityStrategy(entity.type),
      component: decorators[entity.decorator],
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
