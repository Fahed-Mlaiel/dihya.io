// Industrie Controller – Dihya Coding
export const IndustrieController = {
  async createFactory(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
