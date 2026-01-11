from sentiment_analysis.constants.constants import *
from sentiment_analysis.utility.utils import read_yaml
from sentiment_analysis.components.data_ingestion import load_data

def train():
    config = read_yaml(CONFIG_FILE_PATH)
    df = load_data(file_path=config.data_ingestion.raw_data_file_path)
    print(df.head())
    