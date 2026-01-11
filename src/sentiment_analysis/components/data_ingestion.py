from pandas import DataFrame

from sentiment_analysis.utility.utils import read_csv


def load_data(file_path: str) -> DataFrame:
    df = read_csv(path=file_path)
    return df


if __name__ == "__main__":
    from constants.constants import *
    from utility.utils import read_yaml
    config = read_yaml(CONFIG_FILE_PATH)
    df = load_data(file_path=config.data_ingestion.raw_data_file_path)
    print(df.head())