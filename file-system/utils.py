import json


def load_json(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as fp:
        return json.load(fp)
