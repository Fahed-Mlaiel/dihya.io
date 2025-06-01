/**
 * @file solidityGen.js
 * @description Générateur de contrats Solidity pour Dihya Coding : génération sécurisée, validation, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un squelette de contrat Solidity selon les paramètres fournis.
 * @param {object} params
 * @param {string} params.contractName - Nom du contrat
 * @param {string[]} [params.features] - Fonctions à inclure (ex: ['mintable', 'pausable'])
 * @param {string} [params.license='MIT'] - Licence SPDX
 * @param {object} [params.options] - Options avancées (logs, version, etc.)
 * @returns {object} Résultat { success, code, error, timestamp }
 */
export function generateSolidityContract({ contractName, features = [], license = 'MIT', options = {} }) {
  if (!hasConsent()) {
    return {
      success: false,
      code: null,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (!contractName || typeof contractName !== 'string' || !/^[A-Za-z_][A-Za-z0-9_]{2,32}$/.test(contractName)) {
    return {
      success: false,
      code: null,
      error: 'Nom de contrat invalide',
      timestamp: new Date().toISOString()
    };
  }

  const solidityVersion = options.version || '0.8.24';
  let code = `// SPDX-License-Identifier: ${license}
pragma solidity ^${solidityVersion};

contract ${contractName} {
    // Généré par Dihya Coding – ${new Date().toISOString()}
`;

  // Ajout des fonctionnalités de base
  if (features.includes('mintable')) {
    code += `
    address public owner;
    event Mint(address indexed to, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function mint(address to, uint256 amount) public onlyOwner {
        // Implémentation mint
        emit Mint(to, amount);
    }
`;
  }

  if (features.includes('pausable')) {
    code += `
    bool public paused = false;

    modifier whenNotPaused() {
        require(!paused, "Paused");
        _;
    }

    function pause() public onlyOwner {
        paused = true;
    }

    function unpause() public onlyOwner {
        paused = false;
    }
`;
  }

  // Ajout d’un fallback
  code += `
    // Fallback pour recevoir de l’ETH
    receive() external payable {}
}
`;

  if (options.log !== false) {
    logSolidityGenEvent('solidity_contract_generated', {
      contractName: anonymizeContractName(contractName),
      features,
      license,
      timestamp: new Date().toISOString()
    });
  }

  return {
    success: true,
    code,
    error: null,
    timestamp: new Date().toISOString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('solidity_gen_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSolidityGenEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('solidity_gen_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('solidity_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un nom de contrat pour les logs.
 * @param {string} name
 * @returns {string}
 */
function anonymizeContractName(name) {
  if (!name) return '';
  return name.length > 4 ? name.slice(0, 2) + '***' + name.slice(-2) : '***';
}

/**
 * Efface les logs de génération Solidity (droit à l’oubli RGPD).
 */
export function clearLocalSolidityGenLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('solidity_gen_logs');
  }
}