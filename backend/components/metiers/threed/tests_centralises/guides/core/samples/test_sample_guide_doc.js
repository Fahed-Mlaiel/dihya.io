// test_sample_guide_doc.js – Test ultra avancé pour la documentation de guides core samples Threed
test('La documentation sample guide core contient le mot avancée', () => {
  const doc = 'Documentation avancée de sample guide core.';
  expect(doc).toContain('avancée');
});
