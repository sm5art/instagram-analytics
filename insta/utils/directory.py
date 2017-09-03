import os


def get_current_directory(location):
    dir_path = os.path.dirname(os.path.realpath(location))
    return dir_path + "/"