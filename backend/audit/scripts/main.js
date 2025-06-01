/**
 * Dihya – Backend Audit Scripts Entrypoint (Node.js)
 * --------------------------------------------------
 * Point d'entrée unique pour les scripts d'audit backend (multi-stack, multilingue, souveraineté, sécurité).
 * - Permet de lancer les audits d'intégrité, conformité, accessibilité, logs, etc.
 * - Prêt pour intégration Node.js, CI/CD, Codespaces, cloud souverain
 * - Documentation multilingue, logs, conformité RGPD/NIS2, fallback open source
 *
 * 🇫🇷 Point d'entrée scripts d'audit backend Node.js (sécurité, fallback, multilingue)
 * 🇬🇧 Node.js backend audit scripts entry point (secure, fallback, multilingual)
 * 🇦🇪 نقطة دخول سكريبتات تدقيق الباكند (Node.js) مع الأمان والدعم متعدد اللغات
 * ⵣ Amuddu n backend audit scripts Node.js (amatu, fallback, multilingual)
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { program } = require('commander');

const ASSETS_ROOT = path.resolve(__dirname, '../../assets');

const LANGS = {
  fr: {
    start: "🔍 Vérification d’intégrité des assets backend Dihya…",
    ok: "✅ Intégrité vérifiée pour tous les assets.",
    fail: "❌ Intégrité compromise pour :",
    report: "Rapport généré :",
    file: "Fichier",
    hash: "SHA-256",
    status: "Statut",
    missing: "Manquant",
    corrupt: "Corrompu",
    valid: "Valide"
  },
  en: {
    start: "🔍 Checking Dihya backend assets integrity…",
    ok: "✅ All assets integrity verified.",
    fail: "❌ Integrity compromised for:",
    report: "Report generated:",
    file: "File",
    hash: "SHA-256",
    status: "Status",
    missing: "Missing",
    corrupt: "Corrupted",
    valid: "Valid"
  },
  ar: {
    start: "🔍 التحقق من سلامة أصول الباكند Dihya…",
    ok: "✅ تم التحقق من سلامة جميع الأصول.",
    fail: "❌ سلامة الأصول مفقودة لـ:",
    report: "تم إنشاء التقرير:",
    file: "ملف",
    hash: "SHA-256",
    status: "الحالة",
    missing: "مفقود",
    corrupt: "تالف",
    valid: "سليم"
  },
  tzm: {
    start: "🔍 Asnul n tazwart n backend assets Dihya…",
    ok: "✅ Akk assets ttwarnan.",
    fail: "❌ Integrity ur ttwaf ara i:",
    report: "Rapport yettwarnan:",
    file: "Afaylu",
    hash: "SHA-256",
    status: "Addad",
    missing: "Ulac",
    corrupt: "Yettwasel",
    valid: "Yettwasen"
  }
};

function sha256sum(filepath) {
  const data = fs.readFileSync(filepath);
  return crypto.createHash('sha256').update(data).digest('hex');
}

function walkAssets(root) {
  let files = [];
  fs.readdirSync(root).forEach(file => {
    const fullPath = path.join(root, file);
    if (fs.statSync(fullPath).isDirectory()) {
      files = files.concat(walkAssets(fullPath));
    } else {
      files.push(path.relative(root, fullPath));
    }
  });
  return files;
}

function loadReferenceHashes(refFile) {
  if (!fs.existsSync(refFile)) return {};
  return JSON.parse(fs.readFileSync(refFile, 'utf-8'));
}

function main() {
  program
    .option('--lang <lang>', 'Langue du rapport', 'fr')
    .option('--ref <file>', 'Fichier de référence des hashes SHA-256', 'assets_hashes.json')
    .option('--csv', 'Exporter le rapport au format CSV')
    .option('--json', 'Exporter le rapport au format JSON')
    .parse(process.argv);

  const opts = program.opts();
  const L = LANGS[opts.lang] || LANGS.fr;

  console.log(L.start);

  const refPath = path.join(ASSETS_ROOT, opts.ref);
  const refHashes = loadReferenceHashes(refPath);
  const results = [];
  const compromised = [];

  function getAllFiles(dir, base = '') {
    let files = [];
    fs.readdirSync(dir).forEach(file => {
      const fullPath = path.join(dir, file);
      const relPath = path.join(base, file);
      if (fs.statSync(fullPath).isDirectory()) {
        files = files.concat(getAllFiles(fullPath, relPath));
      } else {
        files.push(relPath);
      }
    });
    return files;
  }

  const allFiles = getAllFiles(ASSETS_ROOT);

  allFiles.forEach(relPath => {
    const absPath = path.join(ASSETS_ROOT, relPath);
    const hash = sha256sum(absPath);
    const refHash = refHashes[relPath];
    let status;
    if (refHash && hash === refHash) {
      status = L.valid;
    } else if (refHash) {
      status = L.corrupt;
      compromised.push(relPath);
    } else {
      status = L.missing;
      compromised.push(relPath);
    }
    results.push({
      [L.file]: relPath,
      [L.hash]: hash,
      [L.status]: status
    });
  });

  if (compromised.length > 0) {
    console.log(`${L.fail} ${compromised.join(', ')}`);
  } else {
    console.log(L.ok);
  }

  // Export CSV
  if (opts.csv) {
    const csvPath = path.join(ASSETS_ROOT, "integrity_report.csv");
    const header = [L.file, L.hash, L.status];
    const lines = [header.join(',')].concat(
      results.map(row => header.map(h => row[h]).join(','))
    );
    fs.writeFileSync(csvPath, lines.join('\n'), 'utf-8');
    console.log(`${L.report} ${csvPath}`);
  }

  // Export JSON
  if (opts.json) {
    const jsonPath = path.join(ASSETS_ROOT, "integrity_report.json");
    fs.writeFileSync(jsonPath, JSON.stringify(results, null, 2), 'utf-8');
    console.log(`${L.report} ${jsonPath}`);
  }
}

if (require.main === module) {
  main();
}

/*
 * Utilisation :
 *   node main.js --lang fr --csv --json
 *   node main.js --lang en --ref assets_hashes.json
 *
 * Sécurité : logs, audit, conformité RGPD/NIS2, fallback open source
 * Multilingue : prêt pour i18n (fr, en, ar, tzm)
 * Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
 */
