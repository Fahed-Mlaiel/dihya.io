# VoiceCard

## Description
Carte métier pour la gestion de la voix (synthèse, reconnaissance, analyse) dans les projets IA, VR, AR, etc.

## Fonctions principales
- Synthèse vocale multilingue (TTS)
- Reconnaissance vocale (ASR)
- Analyse de sentiment vocal
- Sécurité (filtrage, anonymisation)

## Exemple d'utilisation
```js
import { synthesizeVoice, recognizeSpeech } from '../voice/VoiceCard';

const audio = synthesizeVoice('Bonjour', 'fr');
const text = recognizeSpeech(audio, 'fr');
```

## Internationalisation
Supporte : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Sécurité
Respect RGPD, anonymisation, logs structurés.

## Extensibilité
Ajoutez vos propres modules vocaux via plugins.
