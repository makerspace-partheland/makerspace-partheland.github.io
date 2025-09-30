const fs = require('fs');
const path = require('path');
const { glob } = require('glob');

async function updateMarkdownImages() {
  console.log('🔍 Suche nach Markdown-Dateien mit <img> Tags...\n');

  const files = await glob('./{_projects,_events,verein,*.md}/**/*.md', {
    ignore: ['**/node_modules/**', '**/vendor/**', '**/_site/**']
  });

  let updated = 0;

  for (const file of files) {
    let content = fs.readFileSync(file, 'utf8');
    let modified = false;

    // Regex für <img> Tags ohne <picture> davor
    const imgRegex = /(?<!<picture>\s*\n\s*<source[^>]*>\s*\n\s*)(<img\s+[^>]*src=["']([^"']+\.(jpg|jpeg|png))["'][^>]*>)/gi;

    content = content.replace(imgRegex, (match, imgTag, src, ext) => {
      // Überspringe wenn bereits in <picture> eingebettet
      if (match.includes('picture')) {
        return match;
      }

      modified = true;

      // Extrahiere Attribute
      const altMatch = imgTag.match(/alt=["']([^"']*)["']/);
      const classMatch = imgTag.match(/class=["']([^"']*)["']/);

      const alt = altMatch ? altMatch[1] : '';
      const classAttr = classMatch ? ` class="${classMatch[1]}"` : '';

      // Erstelle WebP Pfad
      const webpSrc = src.replace(/\.(jpg|jpeg|png)$/i, '.webp');

      return `<picture>
            <source type="image/webp" srcset="${webpSrc}">
            <img src="${src}" alt="${alt}"${classAttr}>
          </picture>`;
    });

    if (modified) {
      fs.writeFileSync(file, content, 'utf8');
      console.log(`✓ ${file}`);
      updated++;
    }
  }

  console.log(`\n✓ ${updated} Dateien aktualisiert`);
}

updateMarkdownImages().catch(console.error);