// eslint.config.js
import parser from "@babel/eslint-parser";

export default [
  {
    files: ["**/*.{js,jsx,ts,tsx}"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      parser,
      parserOptions: {
        requireConfigFile: false,
        babelOptions: {
          presets: ["@babel/preset-react"]
        },
        ecmaFeatures: { jsx: true }
      },
      globals: {
        window: "readonly",
        document: "readonly",
        module: "writable",
        require: "readonly",
        process: "readonly",
        describe: "readonly",
        it: "readonly",
        test: "readonly",
        expect: "readonly",
        beforeAll: "readonly",
        afterAll: "readonly",
        Buffer: "readonly"
      }
    },
    rules: {
      // Beispielregel: keine unbenutzten Variablen
      "no-unused-vars": "warn",
      // Weitere Regeln nach Bedarf
      "no-undef": "error",
      "no-console": "off"
    },
    plugins: {}
  }
];
