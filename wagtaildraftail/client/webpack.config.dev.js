const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const outputPath = path.join('wagtaildraftail', 'static', 'wagtaildraftail');

module.exports = {
  entry: {
    wagtaildraftail: './wagtaildraftail/client/wagtaildraftail.js',
  },
  output: {
    path: outputPath,
    filename: '[name].js',
  },
  plugins: [
    new webpack.NoEmitOnErrorsPlugin(),
    new ExtractTextPlugin('wagtaildraftail.css'),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        use: ['babel-loader'],
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          use: ['css-loader'],
        }),
      },
    ],
  },
};
