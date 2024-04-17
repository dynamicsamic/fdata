import utils.general as general


class UploadDataToDatabase():

    def __init__(self, config):
        self.config = general.read_yml(config)

    def _read_file(self, list_filename):
        return general.prepare_table_list(self.config, list_filename)

    def _prepare_data(self):
        list_file = general.get_file_list(self.config)
        list_filename = general.clear_extension(list_file)
        df = self._read_file(list_filename)
        return df

    def upload_data(self):
        pass
