#!/usr/bin/env node
// Script Node.js pour valider les favicons API backend Dihya (hash, accessibilité, multilingue)
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const FAVICON_DIR = path.join(__dirname, '../api_favicons/svg');
const META_DIR = path.join(__dirname, '../meta');
const LANGS = ["fr", "en", "de", "ar", "es", "it", "pt", "nl", "pl", "tr", "ru", "zh", "kab"];

function sha256sum(filepath) {
  return crypto.createHash('sha256').update(fs.readFileSync(filepath)).digest('hex');
}

function auditFavicons() {
  const report = { date: new Date().toISOString(), favicons: [] };
  fs.readdirSync(FAVICON_DIR).forEach(fname => {
    if (!fname.endsWith('.svg')) return;
    const file = path.join(FAVICON_DIR, fname);
    const meta = path.join(META_DIR, `meta_${fname.replace('.svg','')}.json`);
    const entry = { filename: fname, exists: true, meta: false, hash_ok: false, langs_ok: false, accessibility_ok: false };
    if (fs.existsSync(meta)) {
      entry.meta = true;
      const metaObj = JSON.parse(fs.readFileSync(meta, 'utf-8'));
      entry.hash_ok = metaObj.hash === `sha256:${sha256sum(file)}`;
      entry.langs_ok = LANGS.every(lang => metaObj.alt && metaObj.alt[lang]);
      const acc = metaObj.accessibility || {};
      entry.accessibility_ok = acc.contrast === 'AAA' && acc.aria && acc.tested;
    }
    report.favicons.push(entry);
  });
  fs.writeFileSync(path.join(__dirname, 'audit_favicons_report.json'), JSON.stringify(report, null, 2));
  console.log('Audit terminé. Rapport : audit_favicons_report.json');
}

auditFavicons();
