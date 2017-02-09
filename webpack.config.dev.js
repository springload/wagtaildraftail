/* eslint-disable import/no-extraneous-dependencies */

const path = require('path');
const webpack = require('webpack');

module.exports = {
    // See http://webpack.github.io/docs/configuration.html#devtool
    // devtool: 'inline-source-map',
    entry: {
        draftail: './client/drafteditor.js',
    },
    output: {
        path: path.join(__dirname, 'dist'),
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
