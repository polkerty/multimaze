const env = require('./env-config.js');

module.exports = {
    babelrc: false,
    plugins: [
        ['emotion', { autoLabel: true, sourceMap: true }],
        'inline-react-svg',
        ['transform-define', env],
        ['lodash'],
    ],
    env: {
        development: {
            presets: ['next/babel'],
            compact: false,
        },
        production: {
            presets: [['next/babel', { 'preset-env': { targets: { node: true } } }]],
            plugins: [['emotion', { autoLabel: true, sourceMap: false }]],
        },
        test: {
            presets: [
                [
                    'next/babel',
                    {
                        'preset-env': { modules: 'commonjs' },
                        'transform-runtime': { corejs: false }, // https://github.com/zeit/next.js/issues/7050
                    },
                ],
            ],
        },
    },
};
