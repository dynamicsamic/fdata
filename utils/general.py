import operator
import csv
from django.apps import apps
from fdata.settings import BASE_DIR
import pandas as pd
import yaml
import sqlite3
from os import listdir
from pathlib import Path
from loguru import logger
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
    """
    Получает имена файлов с расширением из дирректории. При обработке не учитывает дирректории
    :param config: конфиг
    :return: список имен файлов с расширениями
    """
    onlyfiles = [f for f in listdir(config['path']['raw_data']) if isfile(join(config['path']['raw_data'], f))]
    return onlyfiles


def clear_extension(list_file: list) -> list:
    """
    Очищает список файлов от расширений, оставляя только имена
    :param list_file: список файлов с расширениями
    :return: список файлов без расширений
    """
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


def prepare_table_list(config: dict, list_filename: list) -> list:
    """
    Подготавливает список имен таблиц, которые должны появиться в базе данных
    :param config: конфиг файл
    :param list_filename: список таблиц из папки где размещены данные
    :return: список имен
    """
    list_tables = []
    for filename in list_filename:
        if filename in get_from_dict(data_dict=config, maplist=['tables']):
            list_tables.append(get_from_dict(
                data_dict=config,
                maplist=['tables', filename, 'db_table_name']
            ))

    return list_tables


def prepare_dir_table(config: dict) -> list:
    """
    Получает список имен файлов, которые необходимо обработать в папке назначения
    :param config: конфиг файл
    :return: список файлов
    """
    dir_tables = []
    for table in config['tables']:
        dir_tables.append(table)
    return dir_tables


def load_data(db_path: str, df, table_name: str):
    con = sqlite3.connect(db_path)
    df['id'] = df.index
    df.to_sql(
        table_name,
        con,
        if_exists="append",
        index=False
    )
