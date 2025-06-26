/**
 * Asset numérique (image, logo, document, etc.).
 */
export interface Asset {
  id: string;
  name: string;
  type: AssetType;
  url: string;
  size: number;
  uploadedAt: string;
  tags?: string[];
}

/**
 * Types d'assets supportés.
 */
export type AssetType = 'image' | 'logo' | 'font' | 'document' | 'video' | 'audio';
