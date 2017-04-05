import React from 'react';
import { Entity } from 'draft-js';
import { Icon } from 'draftail';

const Document = ({ entityKey, children }) => {
  const { title } = Entity.get(entityKey).getData();
  return (
    <span data-tooltip={entityKey} className="RichEditor-link" title={title}>
      <Icon name="icon-doc-full" />
      {children}
    </span>
  );
};

Document.propTypes = {
  entityKey: React.PropTypes.string.isRequired,
  children: React.PropTypes.node.isRequired,
};

export default Document;
