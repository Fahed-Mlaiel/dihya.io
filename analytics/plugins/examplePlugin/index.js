// plugins/examplePlugin/index.js

const express = require('express');
const analyticsRouter = require('./routes/analytics');
const i18n = require('i18n');
const path = require('path');
const helmet = require('helmet');

// Initialize express app
const app = express();

// Security middleware
app.use(helmet());

// Setup internationalization
i18n.configure({
  locales: ['en', 'fr', 'de'],
  directory: path.join(__dirname, 'locales'),
  defaultLocale: 'en',
  objectNotation: true,
  autoReload: true,
  updateFiles: false
});
app.use(i18n.init);

// Analytics routes
app.use('/analytics', analyticsRouter);

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`ExamplePlugin analytics server running on port ${PORT}`);
});

module.exports = app;