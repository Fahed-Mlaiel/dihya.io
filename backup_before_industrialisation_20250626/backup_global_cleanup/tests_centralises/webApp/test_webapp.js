// Test ultra avancé pour le blueprint webapp (React/Next.js)
const { createWebApp } = require("../../webApp/webapp");

test("webApp génère une structure clé en main", () => {
  const app = createWebApp({
    metier: "Inventaire",
    textes: { fr: { titre: "Inventaire Web" } },
    composants: { Accueil: {} },
  });
  expect(app.metier).toBe("Inventaire");
  expect(app).toHaveProperty("textes");
  expect(app).toHaveProperty("composants");
  expect(app.status).toBe("ready");
});
