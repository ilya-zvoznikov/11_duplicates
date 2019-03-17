import os
import sys


def get_directory_path():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        return None
    if not os.path.isdir(directory):
        return None
    return directory


def get_files_in_dir(directory):
    files_dict = {}
    for dir, subdirs, files in os.walk(directory):
        for filename in files:
            fullpath = os.path.join(os.path.abspath(dir), filename)
            fullpath = os.path.realpath(fullpath)
            try:
                file_size = os.path.getsize(fullpath)
            except (OSError,):
                continue
            filename_and_size = (filename, file_size)
            if filename_and_size not in files_dict:
                files_dict[filename_and_size] = [fullpath, ]
            else:
                files_dict[filename_and_size].append(fullpath)
    return files_dict


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
    files_dict = get_files_in_dir(directory)
    print_duplicates(files_dict)
