import React from 'react';
import ReactDOM from 'react-dom';
import { Entity } from 'draft-js';
import DraftailEditor from 'draftail';

import 'draftail/dist/draftail.css';
import './wagtaildraftail.css';

import decorators from './decorators';
import sources from './sources';
import {registerDecorators, getDecorator, registerSources, getSource, registerStrategies, getStrategy} from './registry';

// Register Decorators, Sources and Strategies
registerDecorators(decorators);
registerSources(sources);

// TODO: Use the one from draftail once implemented https://github.com/springload/draftail/issues/48
const getDefaultStrategy = (entityType) => {
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
      control: getSource(entity.source),
      strategy: getStrategy(entity.type) || getDefaultStrategy(entity.type),
      component: getDecorator(entity.decorator),
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

window.wagtailDraftail = {
  // Expose registry methods
  registerDecorators: registerDecorators,
  getDecorator: getDecorator,
  registerSources: registerSources,
  getSource: getSource,
  registerStrategies: registerStrategies,
  getStrategy: getStrategy,

  // Expose basic React methods for basic needs
  createClass: React.createClass,
  createElement: React.createElement,
};

export default initDraftailEditor;
