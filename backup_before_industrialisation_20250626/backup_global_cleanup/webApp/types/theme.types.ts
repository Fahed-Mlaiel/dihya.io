/**
 * Thème UI complet avec branding et palette de couleurs.
 */
export interface Theme {
  id: string;
  name: string;
  palette: ThemePalette;
  isDark: boolean;
  branding: Branding;
}

/**
 * Palette de couleurs d'un thème.
 */
export interface ThemePalette {
  primary: string;
  secondary: string;
  background: string;
  surface: string;
  error: string;
  success: string;
  warning: string;
  info: string;
  text: string;
}

/**
 * Informations de branding associées à un thème.
 */
export interface Branding {
  logoUrl: string;
  faviconUrl?: string;
  slogan?: string;
  description?: string;
}
