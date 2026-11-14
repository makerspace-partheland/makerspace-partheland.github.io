const { test, expect } = require('@playwright/test');

test('Mobiles Menü und Galerie funktionieren im gebauten Seitenstand', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/');
  const menu = page.getByRole('button', { name: 'Menü öffnen' });
  await menu.click();
  await expect(menu).toHaveAttribute('aria-expanded', 'true');
  await expect(page.locator('#navMenu')).toBeVisible();
  await menu.click();
  await expect(menu).toHaveAttribute('aria-expanded', 'false');

  await page.goto('/projekte/reparatur-nachhaltigkeit/chip-tan-generator-reparatur/');
  const gallery = page.locator('.gallery-grid').first();
  await gallery.locator('a[data-index]').first().click();
  const dialog = page.getByRole('dialog', { name: 'Bildergalerie' });
  await expect(dialog).toBeVisible();
  const image = dialog.locator('.modal-content img');
  const firstImage = await image.getAttribute('src');
  await dialog.getByRole('button', { name: 'Nächstes Bild' }).click();
  await expect(image).not.toHaveAttribute('src', firstImage);
  await page.keyboard.press('Escape');
  await expect(dialog).toHaveCount(0);
  expect(errors).toEqual([]);
});
