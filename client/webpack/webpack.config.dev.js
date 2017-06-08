const webpack = require('webpack');

const config = require('./webpack.config.base');

module.exports = Object.assign({}, config, {
  // See http://webpack.github.io/docs/configuration.html#devtool
  devtool: 'inline-source-map',

  plugins: config.plugins.concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('development'),
      },
    }),
  ]),
});
