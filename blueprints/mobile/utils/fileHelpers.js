/**
 * Mock d'upload de fichier (à adapter selon backend)
 * @param {File} file
 * @returns {{success: boolean, fileName: string}}
 */
export function uploadFile(file) {
  // Logique mockée
  return { success: true, fileName: file.name };
}

/**
 * Déclenche le téléchargement d'un fichier depuis une URL
 * @param {string} url
 * @param {string} filename
 */
export function downloadFile(url, filename) {
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
