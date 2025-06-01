// test_seo.js
const { generateRobotsTxt, generateSitemapXml } = require("./template");
const assert = require("assert");

describe("SEO – Template Dihya", () => {
  it("génère un robots.txt multilingue", () => {
    const robots = generateRobotsTxt("en");
    assert(robots.includes("lang=en"));
  });

  it("génère un sitemap.xml multilingue", () => {
    const sitemap = generateSitemapXml(["/home", "/about"], "ar");
    assert(sitemap.includes("lang=ar"));
  });
});
