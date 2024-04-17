import pandas as pd
from pathlib import Path
from loguru import logger
import utils.general as general


class UploadDataToDatabase():

    def __init__(self, config):
        # конфиг
        self.config = general.read_yml(config)
        # имена файлов с расширением
        self.dir_list_file = general.get_file_list(
            config=self.config
        )
        # имена файлов без расширения
        self.dir_list_filename = general.clear_extension(
            list_file=self.dir_list_file
        )
        # имена итоговых таблиц
        self.config_table_list = general.prepare_table_list(
            config=self.config,
            list_filename=self.dir_list_filename
        )
        # имена файлов, которые необходимо загрузить
        self.config_list_file = general.prepare_dir_table(
            config=self.config
        )

    def _get_column(self, df, table):
        # TODO: Остановился на функционале получения колонок для таблицы
        # столбцы из df
        column_df = list(df.columns.values)
        # столбцы из конфига
        match_column = self.config['tables'][table]['column']
        for column in column_df:
            if column not in match_column.keys():
                pass
        print(match_column.keys())


        print(column_df)

    def _read_file(self):
        for name in self.config_list_file:
            if name in self.dir_list_filename:
                path_to_file = Path(f'{self.config['path']['raw_data']}/{name}.csv')
                df = pd.read_csv(path_to_file)
                print(df)
                self._get_column(
                    df=df,
                    table=name
                )
            else:
                logger.warning(f'Файл "{name}" отсутствует в папке источнике.')

    def _prepare_data(self):
        self._read_file()
        return self.config_list_file

    def upload_data(self):
        pass
