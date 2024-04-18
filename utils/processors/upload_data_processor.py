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

    def _read_file(self):
        for name in self.config_list_file:
            if name in self.dir_list_filename:
                path_to_file = Path(f'{self.config['path']['raw_data']}/{name}.csv')
                df = pd.read_csv(path_to_file)
                print(name)
                print(df)
                self._prepare_data(
                    df=df,
                    table=name
                )
            else:
                logger.warning(f'Файл "{name}" отсутствует в папке источнике.')

    def _prepare_data(self, df, table):
        # столбцы из df
        column_df = list(df.columns.values)
        # столбцы из конфига
        match_column = self.config['tables'][table]['column']
        for column in column_df:
            if column not in match_column.keys():
                df.drop(column, axis=1, inplace=True)
                logger.warning(f'Столбец {column} отсутствует в config файле, поэтому был удален')
        df.rename(
            columns=match_column,
            inplace=True
        )

        print(match_column)
        print(df)

        self._load_data(
            df=df,
            tablename=table
        )
        # return df

    def _load_data(self, df, tablename):
        db_table_name = self.config['tables'][tablename]['db_table_name']
        general.load_data(
            db_path=self.config['db_name'],
            df=df,
            table_name=db_table_name
        )


    def upload_data(self):
        self._read_file()
