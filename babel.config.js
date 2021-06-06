module.exports = {
    babelrc: false,
    env: {
        development: {
            presets: ['next/babel'],
            compact: false,
        },
        production: {
            presets: [['next/babel', { 'preset-env': { targets: { node: true } } }]],
        }
    }
};
