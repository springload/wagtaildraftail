/* eslint-disable import/no-extraneous-dependencies */

const path = require('path');
const webpack = require('webpack');

module.exports = {
    // See http://webpack.github.io/docs/configuration.html#devtool
    // devtool: 'inline-source-map',
    entry: {
        wagtaildraftail: './wagtaildraftail/client/wagtaildraftail.js',
    },
    output: {
        path: path.join(__dirname, 'wagtaildraftail', 'static', 'wagtaildraftail'),
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
                    path.join(__dirname, 'wagtaildraftail', 'client'),
                    path.join(__dirname, 'node_modules'),
                ],
            },
            {
                test: /\.s[ac]ss$/,
                loaders: ['style', 'css', 'sass'],
                include: [
                    path.join(__dirname, 'wagtaildraftail', 'client'),
                    path.join(__dirname, 'node_modules'),
                ]
            },
            {
                test: /\.css$/,
                loaders: ['style', 'css'],
                include: [
                    path.join(__dirname, 'wagtaildraftail', 'client'),
                    path.join(__dirname, 'node_modules'),
                ]
            }
        ],
    },
};
