// Sport Controller – Dihya Coding
export const SportController = {
  async createEvent(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
