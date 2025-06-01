// test_services_personne.js
const { createService, listServices } = require("./template");
const assert = require("assert");

describe("Services à la personne – Template Dihya", () => {
  it("crée un service", async () => {
    const srv = await createService({ name: "Test", description: "Desc", lang: "fr", tenant: "t1" });
    assert(srv.id && srv.active);
  });

  it("liste les services d’un tenant", async () => {
    const list = await listServices("t1", "en");
    assert(Array.isArray(list) && list[0].lang === "en");
  });
});
