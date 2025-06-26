// ThemeProvider industriel – React-ready
import { createContext, useContext } from "react";
import { branding } from "./branding";
import { palette } from "./palette";

export const ThemeContext = createContext({ palette, branding });

export const ThemeProvider = ({ children, theme }) => (
  <ThemeContext.Provider value={theme || { palette, branding }}>
    {children}
  </ThemeContext.Provider>
);

export const useTheme = () => useContext(ThemeContext);
