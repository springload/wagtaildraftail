import React from 'react';
import PropTypes from 'prop-types';
import { Portal } from 'draftail';

const propTypes = {
  onModalClose: PropTypes.func.isRequired,
  children: PropTypes.node,
};

const defaultProps = {
  children: null,
};

/**
 * A modal dialog following Wagtail's styles one to one.
 */
class Modal extends React.Component {
  render() {
    const { onModalClose, children } = this.props;
    return (
      <Portal>
        <div
          className="modal fade in"
          tabIndex={-1}
          role="dialog"
          aria-hidden={false}
          style={{ display: 'block' }}
        >
          <div className="modal-dialog">
            <div className="modal-content">
              <button
                onClick={onModalClose}
                type="button"
                className="button close icon text-replace icon-cross"
                data-dismiss="modal"
                aria-hidden={false}
              >
                &times;
              </button>
              <div className="modal-body">
                {children}
              </div>
            </div>
          </div>
        </div>
        <div className="modal-backdrop fade in" />
      </Portal>
    );
  }
}

Modal.propTypes = propTypes;
Modal.defaultProps = defaultProps;

export default Modal;
