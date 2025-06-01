// SEO Controller – Dihya Coding
export const SEOController = {
  async createSeoEntry(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
