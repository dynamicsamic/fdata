import argparse
from utils.processors.upload_data_processor import UploadDataToDatabase

CONFIG = 'utils/config/upload_data_db_config.yml'


def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-c", "--config", help="Full path to config file", required=True)

    # Read arguments from command line
    args = parser.parse_args()

    result = UploadDataToDatabase(args.config)
    result.upload_data()


if __name__ == '__main__':
    main()
