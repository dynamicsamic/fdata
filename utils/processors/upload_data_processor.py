import utils.general as general


class UploadDataToDatabase():

    def __init__(self, config):
        self.config = config

    def prepare_data(self):
        dict_config = general.read_yml(self.config)
        list_file = general.get_file_list(dict_config)
        list_filename = general.clear_extension(list_file)


    def upload_data(self):
        pass
