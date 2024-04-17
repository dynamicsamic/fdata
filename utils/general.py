import operator

import yaml
from os import listdir
from pathlib import Path
from functools import reduce
from os.path import isfile, join


def read_yml(config_path: str) -> dict:
    """
    Преобразовывает yml в dict для удобной работы
    :param config_path: относительный путь до конфиг файла
    :return: dict
    """
    with open(config_path) as fh:
        return yaml.safe_load(fh)


def get_file_list(config: dict) -> list:
    onlyfiles = [f for f in listdir(config['path']['raw_data']) if isfile(join(config['path']['raw_data'], f))]
    return onlyfiles


def clear_extension(list_file: list) -> list:
    clear_list = []
    for file in list_file:
        clear_list.append(Path(file).stem)
    return clear_list


def get_from_dict(data_dict: dict, maplist: list):
    """
    Получает значение по списку вложенности из словаря
    :param data_dict: словарь
    :param maplist: список вложенности
    :return: значение необходимого уровня вложенности
    """
    return reduce(operator.getitem, maplist, data_dict)


def prepare_table_list(config: dict, list_filename: list):
    list_tables = []
    for filename in list_filename:
        # print(filename)
        if filename in get_from_dict(data_dict=config, maplist=['tables']):
            print(filename)
            list_tables.append(get_from_dict(
                data_dict=config,
                maplist=['tables', filename, 'db_table_name']
            ))

    return list_tables
