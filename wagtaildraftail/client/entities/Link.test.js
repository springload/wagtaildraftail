import React from 'react';
import { shallow } from 'enzyme';
import { Entity } from 'draft-js';
import Link from './Link';

describe('Link', () => {
  it('exists', () => {
    expect(Link).toBeDefined();
  });

  it('renders', () => {
    const entityKey = Entity.create('LINK', 'MUTABLE', { url: 'http://example.com/' });
    expect(shallow((
      <Link entityKey={entityKey}>
        <span>Test children</span>
      </Link>
    ))).toMatchSnapshot();
  });

  it('renders email', () => {
    const entityKey = Entity.create('LINK', 'MUTABLE', { url: 'mailto:test@example.com' });
    expect(shallow((
      <Link entityKey={entityKey}>
        <span>Test children</span>
      </Link>
    ))).toMatchSnapshot();
  });
});
