// Services Personne Controller – Dihya Coding
export const ServicesPersonneController = {
  async createService(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
