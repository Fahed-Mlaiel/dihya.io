// Utils Controller – Dihya Coding
export const UtilsController = {
  async createUtil(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
