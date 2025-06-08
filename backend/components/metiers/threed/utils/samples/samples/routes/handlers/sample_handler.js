// Handler JS – Ultra avancé
module.exports = {
  getHandler: () => (req, res) => {
    res.status(200).json({ message: 'Handler OK', user: req.user || null });
  }
};
