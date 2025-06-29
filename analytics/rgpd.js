// rgpd.js
const express = require('express');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const crypto = require('crypto');

const app = express();
app.use(cookieParser());
app.use(bodyParser.json());

// Middleware pour vérifier le consentement RGPD
const checkConsent = (req, res, next) => {
    const consentCookie = req.cookies['rgpd_consent'];
    if (!consentCookie) {
        return res.status(403).json({ message: 'Consentement RGPD requis' });
    }
    next();
};

// Fonction pour anonymiser les données
const anonymizeData = (data) => {
    const hash = crypto.createHash('sha256');
    hash.update(data);
    return hash.digest('hex');
};

// Route pour gérer le consentement RGPD
app.post('/rgpd/consent', (req, res) => {
    const { consent } = req.body;
    if (consent) {
        // Durée de vie du cookie de consentement (1 an)
        res.cookie('rgpd_consent', 'true', { maxAge: 31536000000, httpOnly: true });
        res.json({ message: 'Consentement enregistré' });
    } else {
        res.clearCookie('rgpd_consent');
        res.json({ message: 'Consentement révoqué' });
    }
});

// Route pour collecter des données analytics avec consentement
app.post('/analytics/collect', checkConsent, (req, res) => {
    const { data } = req.body;
    const anonymizedData = anonymizeData(data);
    // Logique pour stocker les données anonymisées
    // ...
    res.json({ message: 'Données collectées et anonymisées' });
});

// Export du module RGPD pour une utilisation dans d'autres parties de l'application
module.exports = {
    app,
    checkConsent,
    anonymizeData
};

// Démarrage du serveur si le fichier est exécuté directement
if (require.main === module) {
    const PORT = process.env.PORT || 3000;
    app.listen(PORT, () => {
        console.log(`RGPD compliance server running on port ${PORT}`);
    });
}