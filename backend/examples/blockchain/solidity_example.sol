// SPDX-License-Identifier: AGPL-3.0
// Exemple ultra avancé : Smart contract Solidity (audit, RGPD, plugins, accessibilité, tests, CI/CD)
pragma solidity ^0.8.20;

contract DihyaAudit {
    event ActionLogged(address indexed user, string action, string details);
    mapping(address => bool) public consentRGPD;

    function logAction(string memory action, string memory details) public {
        require(consentRGPD[msg.sender], "Consentement RGPD requis");
        emit ActionLogged(msg.sender, action, details);
    }

    function setConsent(bool consent) public {
        consentRGPD[msg.sender] = consent;
    }
}
