import express from 'express';
import { generateAnalyticsReport } from './analyticsService';
import { authenticateUser } from './authMiddleware';
import fs from 'fs';
import path from 'path';

const router = express.Router();
router.use(authenticateUser);

router.get('/download-report', async (req, res) => {
  try {
    const userId = req.user.id;
    const reportData = await generateAnalyticsReport(userId);
    const filename = `analytics-report-${userId}-${Date.now()}.pdf`;
    const savePath = path.join(__dirname, 'reports', filename);
    await reportData.toFile(savePath);
    res.download(savePath, filename);
  } catch (err) {
    res.status(500).send('Error downloading report');
  }
});

export default router;