import magenta
import tensorflow
import platform


def print_versions():
    print('python version:' + platform.python_version())
    print('magenta version:' + magenta.__version__)
    print('tensorflow version:' + tensorflow.__version__)
