import os


def clear_directory(directory_path):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if not os.path.isdir(file_path):
            os.remove(file_path)


def make_clear_directory(directory_path):
    if os.path.isdir(directory_path):
        clear_directory(directory_path)
    else:
        os.mkdir(directory_path)


def subdirectories_list(directory_path):
    """
    Get a list of all subdirectories in the specified directory.

    Args:
    directory_path (str): The path to the directory.

    Returns:
    list: A list of all subdirectories in the specified directory.
    """
    return [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
