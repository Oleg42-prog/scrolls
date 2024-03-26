def split_filename(filename):
    """
    Split a filename into its name and extension.

    Args:
    filename (str): The name of the file, including its extension.

    Returns:
    tuple: A tuple containing the file name and the file extension.
    """
    dot_splitted = filename.split('.')
    head, tail = dot_splitted[:-1], dot_splitted[-1]
    name = '.'.join(head)
    extension = tail
    return name, extension


def extract_file_extension(filename):
    _, extension = extract_file_extension(filename)
    return extension
