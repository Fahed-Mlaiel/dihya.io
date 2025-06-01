// Tourisme Controller – Dihya Coding
export const TourismeController = {
  async createAttraction(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
