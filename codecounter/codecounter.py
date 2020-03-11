"""Main module."""
import os


class Counter(object):
    def __init__(self, path='.'):
        if os.path.isdir(path):
            self.path = path
            self.code_files = {}
            self.file_types = []
        else:
            raise NotADirectoryError(path)

    @staticmethod
    def collect_file_extension(file_path):
        return os.path.splitext(file_path)[1]

    def collect_files(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.file_types.append(self.collect_file_extension(file))
                try:
                    self.code_files[self.collect_file_extension(file)]
                except KeyError:
                    self.code_files[self.collect_file_extension(file)] = []

                num_lines = self.read_lines_of_code(os.path.join(root, file))
                self.code_files[self.collect_file_extension(file)].append((os.path.join(root, file), num_lines))
        for key, value in self.code_files.items():
            print(key)
            for each in value:
                print(each)

    @staticmethod
    def read_lines_of_code(file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as infile:
                try:
                    num_lines = infile.readlines()
                except UnicodeDecodeError:
                    num_lines = []
            return len(num_lines)
