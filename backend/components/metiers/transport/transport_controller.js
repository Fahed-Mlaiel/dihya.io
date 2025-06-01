// Transport Controller – Dihya Coding
export const TransportController = {
  async createRoute(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
