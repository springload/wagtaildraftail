const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: {
        wagtaildraftail: './wagtaildraftail/client/wagtaildraftail.js',
    },
    output: {
        path: path.join(__dirname, 'wagtaildraftail', 'static', 'wagtaildraftail'),
        filename: '[name].js',
    },
    plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('development'),
            },
        }),
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                use: ['babel-loader'],
                exclude: /node_modules/,
            },
            {
                test: /\.scss$/,
                use: ['style-loader', 'css-loader', 'sass-loader'],
            },
        ],
    },
};
