// Sante Controller – Dihya Coding
export const SanteController = {
  async createDossier(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
