# Library containing the core functions
import ffmpy
import pathlib 

# ffmpy is a library that does stuff that ffmpeg does
# pathlib will be used to help standardize stuff and check if the directory exists


def convert_dir(directory, target, source):
    print('test')

# source - the extensions that will be converted
# target - the target file types that will be converted to
# directory - the directory which will be converted
# Returns 0 on Success


def verify(directory) -> bool:
    return True
    return False

# Returns true if the directory exists
# Returns false if it is not found

def return_files(directory, extension) -> list:
    file_list = []
    return file_list
# Returns all file paths of files which has the extension given.