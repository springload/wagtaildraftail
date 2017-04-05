import React from 'react';
import { Entity } from 'draft-js';
import { Icon } from 'draftail';

const Link = ({ entityKey, children }) => {
  const { url } = Entity.get(entityKey).getData();

  return (
    <span data-tooltip={entityKey} className="RichEditor-link">
      <Icon name={`icon-${url.indexOf('mailto:') !== -1 ? 'mail' : 'link'}`} />
      {children}
    </span>
  );
};

Link.propTypes = {
  entityKey: React.PropTypes.string.isRequired,
  children: React.PropTypes.node.isRequired,
};

export default Link;
