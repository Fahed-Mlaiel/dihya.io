// test_ressources_humaines.js
// Tests ultra avancés pour le template RH Dihya
const { createEmployee, listEmployees, updateEmployee, deleteEmployee } = require("./template");
const assert = require("assert");

describe("Ressources Humaines – Template Dihya", () => {
  it("crée un employé valide", async () => {
    const emp = await createEmployee({ name: "Test", email: "test@dihya.org", role: "user", lang: "fr", tenant: "t1" });
    assert(emp.id && emp.active);
  });

  it("liste les employés d’un tenant", async () => {
    const list = await listEmployees("t1", {}, "en");
    assert(Array.isArray(list) && list.length >= 1);
    assert(list[0].lang === "en");
  });

  it("met à jour un employé", async () => {
    const updated = await updateEmployee("emp_1", { name: "Alice Updated" }, "t1");
    assert(updated.name === "Alice Updated");
  });

  it("supprime/anonymise un employé", async () => {
    const res = await deleteEmployee("emp_1", "t1", true);
    assert(res === true);
  });
});
