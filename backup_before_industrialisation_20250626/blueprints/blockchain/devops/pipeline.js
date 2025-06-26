// pipeline.js – Service métier DevOps pour CI/CD
function runPipeline(name) {
  if (name === 'deploy') return Promise.resolve({ success: true });
  return Promise.resolve({ success: false });
}
function getPipelineStatus(name) {
  if (name === 'deploy') return 'success';
  return 'failed';
}
module.exports = { runPipeline, getPipelineStatus };
