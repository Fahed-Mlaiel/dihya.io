// Science Controller – Dihya Coding
export const ScienceController = {
  async createExperiment(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
