import React from 'react';
import { shallow } from 'enzyme';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';

// import * as actions from './actions';
import reducer from './reducer';

import PageChooser from './PageChooser';

const store = createStore(reducer, {}, applyMiddleware(thunkMiddleware));

describe('PageChooser', () => {
  it('renders', () => {
    expect(shallow((
      <PageChooser store={store} onModalClose={() => {}} />
    ))).toMatchSnapshot();
    expect(shallow((
      <Provider store={store}>
        <PageChooser onModalClose={() => {}} />
      </Provider>
    ))).toMatchSnapshot();
  });
});
