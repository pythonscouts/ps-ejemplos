class CustomException(Exception):
    pass


def load_data():
    pass  # TODO: Implementar luego


import os


def remove_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
