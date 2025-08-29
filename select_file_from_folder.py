import os
import random

def get_random_file(folder_path):
    """
    Selects a random file from the specified folder.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        str: The full path to the randomly selected file, or None if the folder is empty
             or does not exist.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return None

    files = []

    for f in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, f)):
            files.append(f)

    if not files:
        print(f"No files found in '{folder_path}'.")
        return None

    random_file_name = random.choice(files)
    if os.name == 'nt':
        full_path = folder_path + '/' + random_file_name
    else:
        full_path = folder_path + '\\' + random_file_name

    return full_path

# Example usage:
#import select_file_from_folder as sel
#sel.get_random_file("C:/Users/random_gui/Pictures")
