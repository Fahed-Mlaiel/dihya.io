"""
Plugin d’export RGPD des favicons API backend PNG (hash, logs, anonymisation, version).
"""
import os
import hashlib
import json

def export_rgpd(directory: str, out_file: str = 'favicons_png_rgpd_export.json'):
    export = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            with open(path, 'rb') as f:
                data = f.read()
            export.append({
                'filename': filename,
                'sha256': hashlib.sha256(data).hexdigest(),
                'size': len(data)
            })
    with open(os.path.join(directory, out_file), 'w', encoding='utf-8') as f:
        json.dump(export, f, ensure_ascii=False, indent=2)
    print(f"[PNG_RGPD_EXPORT] Exporté: {out_file}")

if __name__ == '__main__':
    export_rgpd(os.path.dirname(__file__))
