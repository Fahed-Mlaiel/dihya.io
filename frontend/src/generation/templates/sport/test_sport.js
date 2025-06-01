// test_sport.js
const { createSportProject, listSportProjects } = require("./template");
const assert = require("assert");

describe("Sport – Template Dihya", () => {
  it("crée un projet sportif", async () => {
    const prj = await createSportProject({ name: "Test", description: "Desc", lang: "fr", tenant: "t1" });
    assert(prj.id && prj.active);
  });

  it("liste les projets sportifs d’un tenant", async () => {
    const list = await listSportProjects("t1", "en");
    assert(Array.isArray(list) && list[0].lang === "en");
  });
});
