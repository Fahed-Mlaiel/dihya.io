#!/usr/bin/env node
/**
 * Script CLI/API avancé pour la gestion de projets IA/VR/AR, plugins, audit, multilingue, sécurité, génération automatique.
 * Compatible Linux, Codespaces, CI, production.
 * @module main
 */
const yargs = require('yargs');
const { hideBin } = require('yargs/helpers');
const { generateProject, listProjects, auditLog, i18n, plugins } = require('./services');

const argv = yargs(hideBin(process.argv))
  .command('generate [type]', 'Génère un projet (web, mobile, IA, etc.)', (yargs) => {
    yargs.positional('type', {
      describe: 'Type de projet',
      type: 'string',
      choices: ['web', 'mobile', 'ia', 'vr', 'ar']
    });
  })
  .command('list', 'Liste les projets existants')
  .command('plugin [action]', 'Gère les plugins dynamiquement', (yargs) => {
    yargs.positional('action', {
      describe: 'Action plugin',
      type: 'string',
      choices: ['add', 'remove', 'list']
    });
  })
  .option('lang', {
    alias: 'l',
    describe: 'Langue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)',
    type: 'string',
    default: 'fr'
  })
  .demandCommand(1)
  .help()
  .argv;

(async () => {
  if (argv._[0] === 'generate') {
    await generateProject(argv.type, argv.lang);
    auditLog('generate', { type: argv.type, lang: argv.lang });
  } else if (argv._[0] === 'list') {
    await listProjects(argv.lang);
  } else if (argv._[0] === 'plugin') {
    await plugins(argv.action, argv.lang);
  }
})();
