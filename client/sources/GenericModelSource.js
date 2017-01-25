import React from 'react';
import { DraftUtils } from 'draftail';

import ModalPicker from 'wagtailaddons/wagtailmodelchooser/client/components/model-chooser/modal-picker';

const API_BASE_URL = '/admin/modelchooser/api/v1/model/';

class GenericModelSource extends React.Component {
    constructor(props) {
        super(props);
        this.onClose = this.onClose.bind(this);
        this.onSelected = this.onSelected.bind(this);
    }

    onClose() {
        const { onClose } = this.props;
        onClose();
    }

    onSelected(id, data) {
        const { editorState, options, onUpdate } = this.props;
        const fieldName = options.display;
        const nextData = {
            id: id,
            label: data[fieldName],
            contentType: options.contentType,
        };

        const nextState = DraftUtils.createEntity(editorState, options.type, nextData, nextData.label, 'IMMUTABLE');

        onUpdate(nextState);
    }

    render() {
        const { entity, options } = this.props;

        return (
            <ModalPicker
                onChange={this.onSelected}
                onSelect={this.onSelected}
                onClose={this.onClose}
                entity={entity}
                options={{
                    model: options.contentType,
                    modelLabel: options.label,
                    endpoint: `${API_BASE_URL}${options.contentType}`,
                    fields: options.fields,
                    value: null,
                    required: 'false',
                    display: 'name',
                    filter: '',
                    pk_name: 'uuid',
                }}
            />
        );
    }
}

GenericModelSource.propTypes = {
    editorState: React.PropTypes.object.isRequired,
    options: React.PropTypes.object.isRequired,
    entity: React.PropTypes.object,
    onClose: React.PropTypes.func.isRequired,
    onUpdate: React.PropTypes.func.isRequired,
};

export default GenericModelSource;
