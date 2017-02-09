/* eslint-disable import/no-extraneous-dependencies */

const path = require('path');
const webpack = require('webpack');

module.exports = {
    // See http://webpack.github.io/docs/configuration.html#devtool
    // devtool: 'inline-source-map',
    entry: {
        wagtaildraftail: './client/wagtaildraftail.js',
    },
    output: {
        path: path.join(__dirname, 'static'),
        filename: '[name].bundle.js',
    },
    plugins: [
        new webpack.NoErrorsPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('development'),
            },
        }),
    ],
    module: {
        loaders: [
            {
                test: /\.js$/,
                loaders: ['babel'],
                include: [
                    path.join(__dirname, 'client'),
                ],
            },
        ],
    },
};
