// Mobile Controller – Dihya Coding
export const MobileController = {
  async createMobileItem(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
