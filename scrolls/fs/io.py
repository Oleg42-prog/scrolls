import json
import numpy as np


def load_json(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as fp:
        return json.load(fp)


def save_np(file_path, np_array):
    with open(file_path, 'wb') as fp:
        np.save(fp, np_array)
