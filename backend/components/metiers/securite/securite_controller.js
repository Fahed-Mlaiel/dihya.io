// Securite Controller – Dihya Coding
export const SecuriteController = {
  async createIncident(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
