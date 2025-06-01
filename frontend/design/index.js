// src/design/index.js
/**
 * Design system Dihya Coding (accessibilité, i18n, dark mode, responsive, SEO)
 * @module src/design/index.js
 */

export const colors = {
  primary: '#1a237e',
  secondary: '#ffb300',
  accent: '#00bcd4',
  background: '#f5f5f5',
  dark: '#212121',
  error: '#d32f2f',
  success: '#388e3c',
};

export const fontFamilies = {
  default: 'Inter, Arial, sans-serif',
  code: 'Fira Mono, monospace',
};

export const breakpoints = {
  mobile: 480,
  tablet: 768,
  desktop: 1200,
};

export function DihyaButton({ children, onClick, type = 'button', style = {}, ...props }) {
  return (
    <button
      type={type}
      style={{
        background: colors.primary,
        color: '#fff',
        border: 'none',
        borderRadius: 6,
        padding: '10px 20px',
        fontFamily: fontFamilies.default,
        fontWeight: 600,
        cursor: 'pointer',
        ...style,
      }}
      aria-label={children}
      {...props}
      onClick={onClick}
    >
      {children}
    </button>
  );
}

export function DihyaInput({ value, onChange, placeholder, type = 'text', style = {}, ...props }) {
  return (
    <input
      type={type}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      style={{
        border: `1px solid ${colors.primary}`,
        borderRadius: 4,
        padding: '8px 12px',
        fontFamily: fontFamilies.default,
        ...style,
      }}
      aria-label={placeholder}
      {...props}
    />
  );
}
