import os
import pandas as pd
import exceptions as e


def is_valid_L(df: pd.DataFrame) -> bool:
    """
    This method checks whether the DataFrame is in the appropriate format.

    :param df: The DataFrame to be checked.
    :return: True if valid, throw an exception otherwise.
    """
    if df.columns[0] != 'barcode':
        raise e.InvalidDataSetException("column 0 should be 'barcode'")
    if df.columns[1] != 'cell_line_name':
        raise e.InvalidDataSetException("column 1 should be 'cell_line_name'")
    if df.columns[2] != 'compound_name':
        raise e.InvalidDataSetException("column 2 should be 'compound_name'")
    if df.columns[3] != '2D_3D':
        raise e.InvalidDataSetException("column 3 should be '2D_3D'")
    if df.columns[4] != 'dosage':
        raise e.InvalidDataSetException("column 3 should be 'dosage'")
    if df.columns[5] != 'time':
        raise e.InvalidDataSetException("column 4 should be 'time'")
    if not all(isinstance(cell, str) for cell in df['dosage']):
        raise e.InvalidDataSetException("Dosage values are invalid, need to add unit of measurement")
    if not all(isinstance(cell, str) for cell in df['time']):
        raise e.InvalidDataSetException("Time values are invalid, need to add unit of measurement")
    return True


def is_valid_path(path: str, directory: bool = True):
    """
    This method checks whether the DataFrame is in the appropriate format.

    :param path: The path to be checked.
    :param directory: Default is True. If the path is directory - fill True, otherwise - False.
    :return: True if valid, throw an exception otherwise.
    """
    if not os.path.exists(path):
        raise e.InvalidPathException(f"The path '{path}' doesn't exist")
    if directory:
        if not os.path.isdir(path):
            raise e.InvalidDirectoryPathException(f"The path '{path}' should be to directory")
    return True


def is_valid_G(df: pd.DataFrame) -> bool:
    """
    This method checks whether the DataFrame is in the appropriate format.

    :param df: The DataFrame to be checked.
    :return: True if valid, throw an exception otherwise.
    """
    if df.columns[0] != 'UID':
        raise e.InvalidDataSetException("column 0 should be 'UID'")

    return True
