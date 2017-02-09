import React from 'react';
import { Entity } from 'draft-js';
import { Icon } from 'draftail';

export function findLocationEntities(contentBlock, callback) {
    contentBlock.findEntityRanges((character) => {
        const entityKey = character.getEntity();
        return (
            entityKey !== null &&
            Entity.get(entityKey).getType() === 'LOCATION'
        );
    }, callback);
}

const Location = ({ entityKey, children }) => (
    <span data-tooltip={entityKey} className="RichEditor-link">
        <Icon name="icon-site" />
        {children}
    </span>
);

Location.propTypes = {
    entityKey: React.PropTypes.any.isRequired,
    children: React.PropTypes.node.isRequired,
};

export default Location;
