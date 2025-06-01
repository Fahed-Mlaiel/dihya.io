import { recognizeVoice, synthesizeVoice } from './template';

describe('Voice Template', () => {
  it('should synthesize voice (mocked)', async () => {
    window.speechSynthesis = { speak: jest.fn() };
    window.SpeechSynthesisUtterance = function (text) { this.text = text; };
    await expect(synthesizeVoice('Bonjour', 'fr')).resolves.toBeUndefined();
  });

  it('should recognize voice (mocked)', async () => {
    const transcript = 'Test';
    window.SpeechRecognition = function () {
      this.start = () => { this.onresult({ results: [[{ transcript }]] }); };
    };
    await expect(recognizeVoice('fr')).resolves.toBe(transcript);
  });
});
