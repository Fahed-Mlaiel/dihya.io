// test_science.js
const { createProject, listProjects } = require("./template");
const assert = require("assert");

describe("Science – Template Dihya", () => {
  it("crée un projet scientifique", async () => {
    const prj = await createProject({ title: "Test", description: "Desc", lang: "fr", tenant: "t1" });
    assert(prj.id && prj.active);
  });

  it("liste les projets d’un tenant", async () => {
    const list = await listProjects("t1", "en");
    assert(Array.isArray(list) && list[0].lang === "en");
  });
});
