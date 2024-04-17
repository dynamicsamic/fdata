import pandas as pd
from pathlib import Path
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
            path_to_file = Path(f'{self.config['path']['raw_data']}/{name}.csv')
            df = pd.read_csv(path_to_file)
            print(df)

    def _prepare_data(self):
        self._read_file()
        return self.config_list_file

    def upload_data(self):
        pass
