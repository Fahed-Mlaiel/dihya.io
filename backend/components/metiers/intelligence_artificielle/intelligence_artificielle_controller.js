// AI Controller – Dihya Coding
export const AIController = {
  async createModel(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
