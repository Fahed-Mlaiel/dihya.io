// Restauration Controller – Dihya Coding
export const RestaurationController = {
  async createReservation(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
