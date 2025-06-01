// Medias Controller – Dihya Coding
export const MediasController = {
  async createMedia(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
