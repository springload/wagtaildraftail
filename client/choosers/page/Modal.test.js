import React from 'react';
import { shallow } from 'enzyme';
import Modal from './Modal';

describe('Modal', () => {
  it('renders', () => {
    expect(shallow((
      <Modal
        onModalClose={() => {}}
      />
    ))).toMatchSnapshot();
  });
});
