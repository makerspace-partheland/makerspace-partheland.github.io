const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs/promises');
const os = require('node:os');
const path = require('node:path');
const { test } = require('node:test');
const sharp = require('sharp');

test('Bildskript erhält Originale und erzeugt WebP in den vorgesehenen Größen', async () => {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'website-images-'));
  try {
    const images = path.join(directory, 'assets/images');
    await fs.mkdir(images, { recursive: true });
    for (const [name, width] of [['small', 100], ['large', 1400]]) {
      await sharp({ create: { width, height: 100, channels: 3, background: '#448866' } })
        .png().toFile(path.join(images, `${name}.png`));
    }
    const original = await fs.readFile(path.join(images, 'large.png'));
    execFileSync(process.execPath, [path.resolve('scripts/optimize-images.js')], { cwd: directory });
    for (const [name, width] of [
      ['small', 100], ['large', 1400], ['large-400w', 400], ['large-800w', 800], ['large-1200w', 1200],
    ]) {
      const metadata = await sharp(path.join(images, `${name}.webp`)).metadata();
      assert.equal(metadata.format, 'webp');
      assert.equal(metadata.width, width);
    }
    assert.deepEqual(await fs.readFile(path.join(images, 'large.png')), original);
    assert.equal((await fs.readdir(images)).filter(name => name.startsWith('small-')).length, 0);
  } finally {
    await fs.rm(directory, { recursive: true, force: true });
  }
});
