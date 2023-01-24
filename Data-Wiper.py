# Author @PureWizard
# Used to Wipe Data
import os

def get_random_bytes(size):
    """
    Generates random bytes of the specified size.
    :param size: The number of bytes to generate
    :return: A bytes object containing random bytes
    """
    return os.urandom(size)

def wipe_data(file_path):
    """
    Wipes the data in the specified file using random bytes and the specified number of passes.
    :param file_path: The file path to wipe
    """
    with open(file_path, 'wb') as f:
        size = os.path.getsize(file_path)
        for _ in range(3):
            f.write(get_random_bytes(size))

file_path = input("\nAuthor = @PureWizard Aka Mian\nGithub = github.com/PureWizard\n\nEnter the file path to wipe:) ")
wipe_data(file_path)
