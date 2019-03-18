import os
import sys
from collections import defaultdict


def get_directory_path():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        return None
    if not os.path.isdir(directory):
        return None
    return directory


def get_uniqum_filenames_in_dir(directory):
    filenames_dict = defaultdict()
    for dirname, subdirnames, filenames in os.walk(directory):
        for filename in filenames:
            fullpath = os.path.join(os.path.abspath(dirname), filename)
            fullpath = os.path.realpath(fullpath)
            try:
                file_size = os.path.getsize(fullpath)
            except (OSError,):
                continue
            filenames_dict.setdefault(
                (filename, file_size), [],
            ).append(fullpath)
    return filenames_dict


def print_duplicates(files_dict):
    for (filename, size), paths in sorted(files_dict.items()):
        if len(paths) > 1:
            print('{}, size {} bytes'.format(filename, size))
            print(*paths, sep='\n')
            print()


if __name__ == '__main__':
    directory = get_directory_path()
    if not directory:
        exit('Folder path is incorrect or empty')
    files_dict = get_uniqum_filenames_in_dir(directory)
    print_duplicates(files_dict)
