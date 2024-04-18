from utils.processors.upload_data_processor import UploadDataToDatabase

CONFIG = 'utils/config/upload_data_db_config.yml'


def main():
    result = UploadDataToDatabase(CONFIG)
    result.upload_data()


if __name__ == '__main__':
    main()
