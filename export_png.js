const puppeteer = require('puppeteer');
const path = require('path');

// 300dpi: 99mm x 210mm → 1169 x 2480px
// screen default is 96dpi, so scale = 300/96 ≈ 3.125
const SCALE = 3.125;
const W = Math.round(374 * SCALE); // 99mm at 96dpi = 374px
const H = Math.round(793 * SCALE); // 210mm at 96dpi = 793px

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();

  await page.setViewport({ width: 1600, height: 900, deviceScaleFactor: SCALE });

  const filePath = path.resolve(__dirname, 'flyer.html');
  await page.goto('file://' + filePath, { waitUntil: 'networkidle0' });

  // Wait for Google Fonts to load
  await new Promise(r => setTimeout(r, 2000));

  const flyers = await page.$$('.flyer');
  const names = ['flyer_side_A.png', 'flyer_side_B.png'];

  for (let i = 0; i < flyers.length; i++) {
    const outPath = path.resolve(__dirname, names[i]);
    await flyers[i].screenshot({ path: outPath, type: 'png' });
    console.log('Saved: ' + outPath);
  }

  await browser.close();
  console.log('Done. Size target: ~1169x2480px (300dpi print quality)');
})();
