import React from 'react';
import { shallow } from 'enzyme';
import { Entity } from 'draft-js';
import Document from './Document';

describe('Document', () => {
  it('exists', () => {
    expect(Document).toBeDefined();
  });

  it('renders', () => {
    const entityKey = Entity.create('DOCUMENT', 'MUTABLE', { title: 'Test title' });
    expect(shallow((
      <Document entityKey={entityKey}>
        <span>Test children</span>
      </Document>
    ))).toMatchSnapshot();
  });
});
