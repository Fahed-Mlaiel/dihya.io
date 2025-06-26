// Blueprint de génération d'une app mobile (React Native)
function generateMobileApp({ metier, textes, composants }) {
  return `
import React from 'react';
import { View, Text } from 'react-native';

export default function ${metier}Mobile() {
  return (
    <View>
      <Text>${textes.fr.titre}</Text>
      {/* Composants dynamiques */}
    </View>
  );
}
`;
}

module.exports = { generateMobileApp };
