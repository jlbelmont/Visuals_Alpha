from function_config import *
import pandas as pd
from typing import Any



##############
# TEST CASES #
##############

def test_check_dataframe_index(df: pd.DataFrame, expected_index: List[str]) -> None:
    """
    Runs tests to verify that a DataFrame has the expected multi-index.

    Parameters:
        df (pd.DataFrame): The DataFrame to test.
        expected_index (List[str]): The list of expected index level names.
    """
    result = check_dataframe_index(df, expected_index)

    if result:
        print(f"Test passed: DataFrame is indexed by {expected_index}")
    else:
        print(f"Test failed: DataFrame is not indexed by {expected_index}")
        
def check_dataframe_index(df: pd.DataFrame, expected_index: List[str]) -> bool:
    """
    Checks if the DataFrame has a multi-index matching the expected index names.

    Parameters:
        df (pd.DataFrame): The DataFrame to check.
        expected_index (List[str]): The list of expected index level names.

    Returns:
        bool: True if the DataFrame's index matches the expected index, otherwise False.
    """
    # Check if the DataFrame has a multi-index
    if not isinstance(df.index, pd.MultiIndex):
        return False
    
    # Get the levels of the multi-index
    index_levels = df.index.names
    
    # Check if the index levels match the expected levels
    return index_levels == expected_index

def assert_type(*args, **kwargs, data):
    pass

def index_check(expected_index: List[str]):
    pass

def data_check(expected_columns: List[str]):
    pass

#################
# DATA CLEANING #
#################

def dataframe_clean(df: pd.DataFrame):
    pass


