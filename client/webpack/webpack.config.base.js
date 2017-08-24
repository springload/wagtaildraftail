const path = require('path');
const webpack = require('webpack');
const autoprefixer = require('autoprefixer');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

const autoprefixerConfig = {
  browsers: ['> 1%', 'ie 11'],
};

const stats = {
  // Add chunk information (setting this to `false` allows for a less verbose output)
  chunks: false,
  // Add the hash of the compilation
  hash: false,
  // `webpack --colors` equivalent
  colors: true,
  // Add information about the reasons why modules are included
  reasons: false,
  // Add webpack version information
  version: false,
  // Set the maximum number of modules to be shown
  maxModules: 0,
};

const isProduction = process.env.NODE_ENV === 'production';

const extractSass = new ExtractTextPlugin('wagtaildraftail.css');

const outputPath = path.join(__dirname, '..', '..', 'wagtaildraftail', 'static', 'wagtaildraftail');

module.exports = {
  entry: {
    wagtaildraftail: [
      './client/utils/polyfills.js',
      './client/wagtaildraftail.js',
    ],
  },

  output: {
    path: outputPath,
    filename: '[name].js',
  },

  plugins: [
    new webpack.NoEmitOnErrorsPlugin(),
    new BundleAnalyzerPlugin({
      // Can be `server`, `static` or `disabled`.
      analyzerMode: 'static',
      // Path to bundle report file that will be generated in `static` mode.
      reportFilename: path.join(__dirname, 'webpack-stats.html'),
      // Automatically open report in default browser
      openAnalyzer: false,
      logLevel: isProduction ? 'info' : 'warn',
    }),
    extractSass,
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        use: ['babel-loader'],
        exclude: /node_modules/,
      },
      {
        test: /\.(scss|css)$/,
        use: extractSass.extract({
          use: [
            {
              loader: 'css-loader',
              options: {
                sourceMap: !isProduction,
                minimize: isProduction ? {
                  autoprefixer: autoprefixerConfig,
                } : false,
              },
            },
            {
              loader: 'postcss-loader',
              options: {
                sourceMap: !isProduction,
                plugins: () => [
                  autoprefixer(autoprefixerConfig),
                ],
              },
            },
            {
              loader: 'sass-loader',
              options: {
                sourceMap: !isProduction,
              },
            },
          ],
        }),
      },
    ],
  },

  stats: stats,

  // Some libraries import Node modules but don't use them in the browser.
  // Tell Webpack to provide empty mocks for them so importing them works.
  node: {
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
  },
};
