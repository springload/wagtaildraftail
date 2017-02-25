import React from 'react';
import { Entity } from 'draft-js';
import Document from './Document';
import { shallow } from 'enzyme';

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
  })
});
