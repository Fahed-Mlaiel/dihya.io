// test_tourisme.js
const { createTourismProject, listTourismProjects } = require("./template");
const assert = require("assert");

describe("Tourisme – Template Dihya", () => {
  it("crée un projet touristique", async () => {
    const prj = await createTourismProject({ name: "Test", description: "Desc", lang: "fr", tenant: "t1" });
    assert(prj.id && prj.active);
  });

  it("liste les projets touristiques d’un tenant", async () => {
    const list = await listTourismProjects("t1", "en");
    assert(Array.isArray(list) && list[0].lang === "en");
  });
});
