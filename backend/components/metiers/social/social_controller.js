// Social Controller – Dihya Coding
export const SocialController = {
  async createPost(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
