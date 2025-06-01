#!/usr/bin/env node
// Audit et test Node.js ultra avancé des illustrations backend Dihya
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ILLUSTRATION_DIR = __dirname;
const META_DIR = __dirname;
const LANGS = ["fr", "en", "de", "ar", "es", "it", "pt", "nl", "pl", "tr", "ru", "zh", "kab"];

function sha256sum(filepath) {
  return crypto.createHash('sha256').update(fs.readFileSync(filepath)).digest('hex');
}

function auditIllustrations() {
  const report = { date: new Date().toISOString(), illustrations: [] };
  fs.readdirSync(ILLUSTRATION_DIR).forEach(fname => {
    if (!fname.endsWith('.svg')) return;
    const file = path.join(ILLUSTRATION_DIR, fname);
    const meta = path.join(META_DIR, `meta_${fname.replace('.svg','')}.json`);
    const entry = { filename: fname, exists: true, meta: false, hash_ok: false, langs_ok: false, accessibility_ok: false, rgpd_ok: false, svg_valid: false };
    if (fs.existsSync(meta)) {
      entry.meta = true;
      const metaObj = JSON.parse(fs.readFileSync(meta, 'utf-8'));
      entry.hash_ok = metaObj.hash === `sha256:${sha256sum(file)}`;
      entry.langs_ok = LANGS.every(lang => metaObj.alt && metaObj.alt[lang]);
      const acc = metaObj.accessibility || {};
      entry.accessibility_ok = acc.contrast === 'AAA' && acc.aria && acc.tested;
      const rgpd = metaObj.rgpd || {};
      entry.rgpd_ok = rgpd.personal_data === false && rgpd.anonymized && rgpd.compliance;
    }
    try {
      const content = fs.readFileSync(file, 'utf-8');
      entry.svg_valid = content.trim().startsWith('<svg') && content.trim().endsWith('</svg>');
    } catch {
      entry.svg_valid = false;
    }
    report.illustrations.push(entry);
  });
  fs.writeFileSync(path.join(ILLUSTRATION_DIR, 'audit_illustrations_report.json'), JSON.stringify(report, null, 2));
  console.log('Audit terminé. Rapport : audit_illustrations_report.json');
}

auditIllustrations();
