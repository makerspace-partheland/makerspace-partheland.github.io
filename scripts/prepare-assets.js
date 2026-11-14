const fs = require('node:fs');

fs.mkdirSync('assets/js', { recursive: true });
fs.copyFileSync(require.resolve('alpinejs/dist/cdn.min.js'), 'assets/js/alpine.min.js');
