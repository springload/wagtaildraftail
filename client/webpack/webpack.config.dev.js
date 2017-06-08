const webpack = require('webpack');

const config = require('./webpack.config.base');

module.exports = Object.assign({}, config, {
  plugins: config.plugins.concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('development'),
      },
    }),
  ]),
});
