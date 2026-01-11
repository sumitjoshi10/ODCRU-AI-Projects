import yaml
import pandas as pd
from pandas import DataFrame
from box import ConfigBox

from sentiment_analysis.utility.utils_helper import resolve_config

def read_csv(path: str) -> DataFrame:
    """Reads a CSV file and returns a DataFrame.
    Args:
        path (str): path like input
    Errors:
        exception: File not found or any other exception while reading CSV file
    Returns:
        pd.DataFrame: DataFrame containing the CSV data
    """
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()
        df = df.dropna(subset=['text', 'sentiment'])
        return df
    except Exception as e:
        raise e
    
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (str): path like input
    Errors:
        exception: Empty file or any other exception while reading yaml file
    Returns:
        ConfigBox: A ConfigBox object containing the loaded YAML data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            content = resolve_config(content)
            return ConfigBox(content)
    except Exception as e:
        raise e  