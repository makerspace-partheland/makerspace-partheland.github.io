const sharp = require('sharp');
const fs = require('fs');
const path = require('path');
const { glob } = require('glob');

const ASSETS_DIR = './assets/images';
const QUALITY = 85;
const RESPONSIVE_SIZES = [400, 800, 1200];

// Farben für Console Output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  blue: '\x1b[34m',
  yellow: '\x1b[33m',
  red: '\x1b[31m'
};

async function optimizeImages() {
  console.log(`${colors.blue}🔍 Suche nach Bildern in ${ASSETS_DIR}...${colors.reset}\n`);

  // Finde alle JPG, JPEG und PNG Dateien
  const images = await glob(`${ASSETS_DIR}/**/*.{jpg,jpeg,png,JPG,JPEG,PNG}`, {
    ignore: ['**/*.webp', '**/favicons/**']
  });

  console.log(`${colors.green}✓ ${images.length} Bilder gefunden${colors.reset}\n`);

  let converted = 0;
  let skipped = 0;
  let errors = 0;

  for (const imagePath of images) {
    try {
      const ext = path.extname(imagePath).toLowerCase();
      const basename = path.basename(imagePath, ext);
      const dirname = path.dirname(imagePath);

      // WebP Pfad
      const webpPath = path.join(dirname, `${basename}.webp`);

      // Überspringe wenn WebP bereits existiert und neuer ist
      if (fs.existsSync(webpPath)) {
        const originalStat = fs.statSync(imagePath);
        const webpStat = fs.statSync(webpPath);

        if (webpStat.mtime >= originalStat.mtime) {
          skipped++;
          continue;
        }
      }

      // Konvertiere zu WebP
      await sharp(imagePath)
        .webp({ quality: QUALITY })
        .toFile(webpPath);

      // Hole Dateigrößen
      const originalSize = fs.statSync(imagePath).size;
      const webpSize = fs.statSync(webpPath).size;
      const savings = ((1 - webpSize / originalSize) * 100).toFixed(1);

      console.log(`${colors.green}✓${colors.reset} ${path.relative('.', imagePath)}`);
      console.log(`  → WebP: ${formatBytes(webpSize)} (${savings}% kleiner)\n`);

      converted++;

      // Erstelle responsive Versionen für größere Bilder
      const metadata = await sharp(imagePath).metadata();
      if (metadata.width > 800) {
        for (const size of RESPONSIVE_SIZES) {
          if (size < metadata.width) {
            const responsivePath = path.join(dirname, `${basename}-${size}w.webp`);
            await sharp(imagePath)
              .resize(size, null, { withoutEnlargement: true })
              .webp({ quality: QUALITY })
              .toFile(responsivePath);
          }
        }
      }

    } catch (error) {
      console.error(`${colors.red}✗ Fehler bei ${imagePath}: ${error.message}${colors.reset}\n`);
      errors++;
    }
  }

  // Zusammenfassung
  console.log(`\n${colors.blue}${'='.repeat(50)}${colors.reset}`);
  console.log(`${colors.green}✓ Konvertiert: ${converted}${colors.reset}`);
  console.log(`${colors.yellow}⊘ Übersprungen: ${skipped}${colors.reset}`);
  if (errors > 0) {
    console.log(`${colors.red}✗ Fehler: ${errors}${colors.reset}`);
  }
  console.log(`${colors.blue}${'='.repeat(50)}${colors.reset}\n`);
}

function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}

// Starte Optimierung
optimizeImages().catch(console.error);