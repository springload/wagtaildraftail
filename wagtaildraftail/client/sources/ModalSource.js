import React from 'react';
import { Entity, AtomicBlockUtils, RichUtils } from 'draft-js';

const $ = global.jQuery;

class ModalSource extends React.Component {
    constructor(props) {
        super(props);
        this.onClose = this.onClose.bind(this);
        this.onConfirm = this.onConfirm.bind(this);
        this.onConfirmAtomicBlock = this.onConfirmAtomicBlock.bind(this);
    }

    onConfirm(data) {
        const { editorState, options, onUpdate } = this.props;
        const entityKey = Entity.create(options.type, 'MUTABLE', data);
        const nextState = RichUtils.toggleLink(editorState, editorState.getSelection(), entityKey);

        onUpdate(nextState);
    }

    onConfirmAtomicBlock(data) {
        const { editorState, options, onUpdate } = this.props;
        const entityKey = Entity.create(options.type, 'IMMUTABLE', data);
        const nextState = AtomicBlockUtils.insertAtomicBlock(editorState, entityKey, ' ');

        onUpdate(nextState);
    }

    onClose(e) {
        const { onClose } = this.props;
        e.preventDefault();

        onClose();
    }

    componentWillUnmount() {
        $(document.body).off('hidden.bs.modal', this.onClose);
    }

    render() {
        return <div />;
    }
}

ModalSource.propTypes = {
    editorState: React.PropTypes.object.isRequired,
    options: React.PropTypes.object.isRequired,
    entity: React.PropTypes.object,
    onUpdate: React.PropTypes.func.isRequired,
    onClose: React.PropTypes.func.isRequired,
};

ModalSource.defaultProps = {
    entity: null,
};

export default ModalSource;
