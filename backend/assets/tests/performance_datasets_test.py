import os, time, json, csv, yaml, toml, xml.etree.ElementTree as ET

def measure_load_time(fname, loader):
    start = time.time()
    loader(fname)
    return time.time() - start

def load_json(fname):
    with open(fname) as f:
        json.load(f)

def load_csv(fname):
    with open(fname) as f:
        list(csv.reader(f))

def load_yaml(fname):
    with open(fname) as f:
        yaml.safe_load(f)

def load_toml(fname):
    toml.load(fname)

def load_xml(fname):
    ET.parse(fname)

def main():
    loaders = {
        '.json': load_json,
        '.csv': load_csv,
        '.yaml': load_yaml,
        '.toml': load_toml,
        '.xml': load_xml
    }
    for fname in os.listdir('.'):
        ext = os.path.splitext(fname)[1]
        if ext in loaders:
            t = measure_load_time(fname, loaders[ext])
            print(f"{fname}: {t:.4f} sec")

if __name__ == '__main__':
    main()
