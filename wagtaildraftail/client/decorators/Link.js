import PropTypes from 'prop-types';
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
  entityKey: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
};

export default Link;
