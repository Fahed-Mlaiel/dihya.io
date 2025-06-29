module.exports = {
  defaultPattern: 'pattern_example_1',
  availablePatterns: [
    'pattern_example_1',
    'pattern_example_2'
  ],
  getPatternPath: (name) => {
    const map = {
      pattern_example_1: 'svg/pattern_example_1.svg',
      pattern_example_2: 'png/pattern_example_2.png'
    };
    return map[name] || null;
  }
};
