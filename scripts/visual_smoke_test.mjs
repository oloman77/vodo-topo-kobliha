import { chromium } from 'playwright';
import { mkdirSync, writeFileSync } from 'node:fs';

const SITE = 'https://vodotopokobliha.cz/';
const SIZES = [
  ['mobile-320', 320, 720],
  ['mobile-375', 375, 812],
  ['mobile-390', 390, 844],
  ['tablet-768', 768, 1024],
  ['desktop-1024', 1024, 768],
  ['desktop-1440', 1440, 900],
];
mkdirSync('visual-results', { recursive: true });
const browser = await chromium.launch({ headless: true });
const results = [];
let errors = 0;
try {
  for (const [name, width, height] of SIZES) {
    const context = await browser.newContext({
      viewport: { width, height }, deviceScaleFactor: 1,
      isMobile: name.startsWith('mobile'), hasTouch: name.startsWith('mobile'),
      locale: 'cs-CZ'
    });
    const page = await context.newPage();
    const failures = [];
    const warnings = [];
    const status = await page.goto(SITE, { waitUntil: 'domcontentloaded', timeout: 30000 });
    if (!status || status.status() !== 200) failures.push('Initial HTML HTTP status not 200');
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(450);
    const imageNodes = page.locator('main img');
    const imageCount = await imageNodes.count();
    if (imageCount !== 6) failures.push('Expected 6 reference images, found ' + imageCount);
    for (let i = 0; i < imageCount; i++) {
      const img = imageNodes.nth(i);
      await img.scrollIntoViewIfNeeded();
      try {
        await img.evaluate(el => new Promise((resolve, reject) => {
          if (el.complete) return el.naturalWidth > 0 ? resolve(true) : reject(Error('Empty image'));
          el.addEventListener('load', () => resolve(true), { once:true });
          el.addEventListener('error', () => reject(Error('Image loading failed')), { once:true });
        }), { timeout: 15000 });
      } catch (err) {
        failures.push('Image #' + (i + 1) + ' did not load: ' + String(err).slice(0,140));
      }
    }
    await page.locator('footer').scrollIntoViewIfNeeded();
    await page.waitForTimeout(250);
    const details = await page.evaluate(() => {
      const header = document.querySelector('header');
      const nav = document.querySelector('.nav');
      const anchors = [...document.querySelectorAll('.nav a')];
      const navRects = anchors.map(a => ({label:a.textContent.trim(),top:a.getBoundingClientRect().top,right:a.getBoundingClientRect().right}));
      const nr = nav.getBoundingClientRect();
      const services = [...document.querySelectorAll('.service')];
      const iconRects = services.map(s=>s.getBoundingClientRect().top);
      const pics = [...document.querySelectorAll('main img')].map(img => ({
        src: img.currentSrc,
        loaded: img.complete && img.naturalWidth > 0,
        naturalWidth: img.naturalWidth,
        naturalHeight: img.naturalHeight
      }));
      const bg = getComputedStyle(document.querySelector('footer')).backgroundImage;
      const invalidAnchors = [...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.getAttribute('href').slice(1))).map(a=>a.getAttribute('href'));
      return {
        viewport: innerWidth,
        documentWidth: document.documentElement.scrollWidth,
        headerHeight: Math.round(header.getBoundingClientRect().height),
        navWrap: getComputedStyle(nav).flexWrap,
        navOneRow: navRects.every(x => Math.abs(x.top-navRects[0].top)<2),
        navAllVisible: navRects.every(x => x.right<=nr.right + 2),
        navScrollWidth: nav.scrollWidth,
        navClientWidth: nav.clientWidth,
        servicesOneRow: iconRects.every(y => Math.abs(y-iconRects[0])<2),
        pictures: pics,
        footerBackground: bg,
        invalidAnchors,
        tel: [...document.querySelectorAll('a[href^="tel:"]')].length,
        mailto: [...document.querySelectorAll('a[href^="mailto:"]')].length,
        title: document.title,
      };
    });
    if (details.documentWidth > details.viewport + 5) failures.push('Document has horizontal overflow');
    if (!details.navOneRow) failures.push('Navigation wraps to more than one row');
    if (width <= 880 && !details.servicesOneRow) failures.push('Service icons not in one row');
    if (!details.navAllVisible) warnings.push('One or more navigation items extend beyond visible navigation viewport');
    if (details.invalidAnchors.length) failures.push('Broken hash anchors: ' + details.invalidAnchors.join(','));
    if (details.pictures.some(p => !p.loaded)) failures.push('Some pictures are not loaded');
    if (details.pictures.some(p => !p.src.includes('/assets/optimized/'))) failures.push('External or unoptimized reference photo found');
    if (!details.footerBackground.includes('/assets/optimized/')) failures.push('Footer background is not localized');
    if (details.tel < 1 || details.mailto < 1) failures.push('Phone or email link missing');
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
    await page.waitForTimeout(150);
    await page.screenshot({path:'visual-results/'+name+'.png',fullPage:true,animations:'disabled'});
    results.push({ name, width, height, status: status?.status(), ...details, failures, warnings });
    errors += failures.length;
    console.log(JSON.stringify({name,width,failures,warnings,imagesLoaded:details.pictures.filter(x=>x.loaded).length,navOneRow:details.navOneRow,servicesOneRow:details.servicesOneRow,documentWidth:details.documentWidth,viewport:details.viewport}));
    await context.close();
  }
} finally {
  await browser.close();
}
writeFileSync('visual-results/results.json', JSON.stringify(results,null,2));
console.log('VISUAL CHECK COMPLETE: ' + SIZES.length + ' viewport sizes, ' + errors + ' errors.');
if (errors) process.exitCode = 1;
