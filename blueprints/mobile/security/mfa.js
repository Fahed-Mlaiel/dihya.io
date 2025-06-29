// MFA (Multi-Factor Authentication) – Sécurité avancée
export function sendMfaCode(user) {
  // Simule l’envoi d’un code MFA (SMS, email, app)
  const code = Math.floor(100000 + Math.random() * 900000);
  // Ici, on log le code pour l’exemple (à remplacer par un vrai envoi)
  console.log(`MFA code for ${user.email}: ${code}`);
  return code;
}
export function verifyMfaCode(user, code, input) {
  // Pour l’exemple, on suppose que le code est stocké côté client/session
  return code === input;
}
