import os
import json
from deep_translator import GoogleTranslator

def translate_text(text, target='en'):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except Exception:
        return text

def translate_index(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for entry in data:
        for field in ['name', 'description', 'sector']:
            if field in entry and entry[field]:
                entry[field] = translate_text(entry[field], 'en')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print('index.json translated to English.')

if __name__ == '__main__':
    translate_index('index.json')
