// RH Controller – Dihya Coding
export const RHController = {
  async createEmployee(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
