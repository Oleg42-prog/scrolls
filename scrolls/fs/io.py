import json
import pickle
import numpy as np


def append_to_file(file_path, content, end='\n', encoding='utf-8'):
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(content + end)


def load_json(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as fp:
        return json.load(fp)


def save_np(file_path, np_array):
    with open(file_path, 'wb') as fp:
        np.save(fp, np_array)


def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data


def save_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
