import os, json, csv, yaml, random, string, toml, xml.etree.ElementTree as ET

def fuzz_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def mutate_json_file(fname):
    with open(fname) as f:
        data = json.load(f)
    # Fuzz: change a random string field
    for entry in data:
        for k, v in entry.items():
            if isinstance(v, str):
                entry[k] = fuzz_string()
                break
        break
    with open('fuzzed_' + fname, 'w') as f:
        json.dump(data, f)

def mutate_csv_file(fname):
    with open(fname) as f:
        rows = list(csv.reader(f))
    if len(rows) > 1:
        rows[1][1] = fuzz_string()
    with open('fuzzed_' + fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def mutate_yaml_file(fname):
    with open(fname) as f:
        data = yaml.safe_load(f)
    if isinstance(data, list) and data and isinstance(data[0], dict):
        for k in data[0]:
            if isinstance(data[0][k], str):
                data[0][k] = fuzz_string()
                break
    with open('fuzzed_' + fname, 'w') as f:
        yaml.dump(data, f)

def mutate_toml_file(fname):
    data = toml.load(fname)
    for section in data:
        if isinstance(data[section], list) and data[section]:
            for k in data[section][0]:
                if isinstance(data[section][0][k], str):
                    data[section][0][k] = fuzz_string()
                    break
            break
    with open('fuzzed_' + fname, 'w') as f:
        toml.dump(data, f)

def mutate_xml_file(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    for elem in root.iter():
        if elem.text:
            elem.text = fuzz_string()
            break
    tree.write('fuzzed_' + fname)

def main():
    for fname in os.listdir('.'):
        if fname.endswith('.json'):
            mutate_json_file(fname)
        elif fname.endswith('.csv'):
            mutate_csv_file(fname)
        elif fname.endswith('.yaml'):
            mutate_yaml_file(fname)
        elif fname.endswith('.toml'):
            mutate_toml_file(fname)
        elif fname.endswith('.xml'):
            mutate_xml_file(fname)
    print('Fuzzing/mutation terminé. Fichiers fuzzed_* générés.')

if __name__ == '__main__':
    main()
