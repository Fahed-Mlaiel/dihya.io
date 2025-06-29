// api/index.js

const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const i18n = require('i18n');
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');
const analyticsRouter = require('./routes/analytics');
const { errorHandler, notFoundHandler } = require('./middleware/errorHandlers');

// Initialize express app
const app = express();

// Security middlewares
app.use(helmet());
app.use(cors());

// Body parser middleware
app.use(express.json());

// Internationalization setup
i18n.configure({
  locales: ['en', 'fr', 'de', 'es'],
  directory: __dirname + '/locales',
  defaultLocale: 'en',
  objectNotation: true,
  updateFiles: false,
  api: {
    '__': 't', // now req.t can be used for translation
  },
});

app.use(i18n.init);

// API Documentation
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Analytics routes
app.use('/analytics', analyticsRouter);

// Error handling middleware
app.use(notFoundHandler);
app.use(errorHandler);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;