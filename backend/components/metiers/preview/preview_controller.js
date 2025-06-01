// Preview Controller – Dihya Coding
export const PreviewController = {
  async createPreview(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
