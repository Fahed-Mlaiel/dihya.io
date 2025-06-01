// Mock multitenancy (contexte tenant)
function getTenantContext(tenant) { return { tenant, ctx: 'ok' }; }
module.exports = { getTenantContext };
