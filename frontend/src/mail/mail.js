/**
 * Module d'envoi d'e-mails sécurisé et multilingue pour Dihya
 * @module mail/mail
 * @author Dihya Team
 * @description Envoi d'e-mails transactionnels, multilingues, auditables, RGPD.
 * @i18n Support: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, user
 * @security SMTP sécurisé, logs, audit, RGPD
 */

const nodemailer = require('nodemailer');
const { logAudit } = require('../../backend/utils/audit');

/**
 * Envoie un e-mail transactionnel sécurisé et multilingue.
 * @param {object} options - { to, subject, text, html, lang, userId }
 * @returns {Promise<object>} Résultat de l'envoi
 */
async function sendMail(options) {
  // Validation et logs
  if (!options.to || !options.subject || !options.text) {
    throw new Error('Paramètres e-mail invalides');
  }
  logAudit({ action: 'send_mail', userId: options.userId, lang: options.lang });

  // Transport sécurisé (adapter selon config réelle)
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    secure: true,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });

  const mailOptions = {
    from: process.env.MAIL_FROM,
    to: options.to,
    subject: options.subject,
    text: options.text,
    html: options.html,
  };

  return transporter.sendMail(mailOptions);
}

module.exports = { sendMail };
