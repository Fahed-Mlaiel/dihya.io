// Handler imbriqué JS – Ultra avancé
module.exports = {
  getNestedHandler: () => (req, res) => {
    res.status(200).json({ message: 'Nested Handler OK', nested: true });
  }
};
