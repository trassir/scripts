import os
import pickle

from helpers import get_logger

logger = get_logger()


def save(file_path, data):
    """Save data to pkl file

    Args:
        file_path (str): Config file path
        data (any): Data to save

    Returns:
        str: full file path
    """

    with open(file_path, "wb") as opened_file:
        pickle.dump(data, opened_file)

    return os.path.abspath(file_path)


def load(file_path, default_type=dict):
    """Load data from pkl file

    Args:
        file_path (str): Config file path
        default_type (type): Default data type

    Returns:
        default_type: default type if can't load

    """
    data = default_type()
    if os.path.isfile(file_path):
        try:
            with open(file_path, "rb") as opened_file:
                data = pickle.load(opened_file)
        except (EOFError, IndexError, ValueError, TypeError):
            logger.warning("Broken or empty pkl file", exc_info=True)

    return data
