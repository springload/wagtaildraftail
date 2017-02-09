const path = require('path');
const webpack = require('webpack');

const config = require('./webpack.config.dev');

config.plugins = [
    new webpack.NoEmitOnErrorsPlugin(),
    new webpack.DefinePlugin({
        'process.env': {
            NODE_ENV: JSON.stringify('production'),
        },
    }),
];

module.exports = config;
