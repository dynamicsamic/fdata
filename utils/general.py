import yaml
from os import listdir
from pathlib import Path
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


def prepare_table_listt(config: dict):
    list_tables = []
    print(config['tables']['stats_laptime'])
    for table in config['tables']:
        print(table)
        list_tables.append(table['source_csv'])

    return list_tables
