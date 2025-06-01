// Hotellerie Controller – Dihya Coding
export const HotellerieController = {
  async createReservation(req, res) {
    res.status(201).json({ success: true });
  },
  async exportData(req, res) {
    res.json({ data: [] });
  }
};
