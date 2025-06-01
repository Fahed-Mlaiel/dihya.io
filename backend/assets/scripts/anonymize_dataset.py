# Dihya Backend Assets – Exemple de Script d’Anonymisation

```python
# anonymize_dataset.py
import json

def anonymize(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)
    for entry in data:
        entry['email'] = 'anonymous@example.com'
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
```
