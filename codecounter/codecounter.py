"""Main module."""
import os
import pandas


class Counter(object):
    def __init__(self, path='.'):
        if os.path.isdir(path):
            self.path = path
            self.code_files = {}
            self.file_types = []
            self.dataframe = pandas.DataFrame()
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
                if num_lines > 0 and '.git' not in file and '.git' not in root and '.lock' not in file:
                    self.code_files[self.collect_file_extension(file)].append({"File": os.path.join(root, file),
                                                                            "Number_Of_Lines": num_lines})

    @staticmethod
    def read_lines_of_code(file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as infile:
                try:
                    num_lines = infile.readlines()
                except UnicodeDecodeError:
                    num_lines = []
            return len(num_lines)

    def build_dataframe(self):
        self.dataframe = pandas.DataFrame(columns=['FileType', 'File', 'Number_Of_Lines'])
        for code_type, list_of_files in self.code_files.items():
            for code_file in list_of_files:
                self.dataframe =self.dataframe.append({'FileType': code_type,
                                       'File': code_file['File'],
                                       'Number_Of_Lines': code_file['Number_Of_Lines']}, ignore_index=True)

    def export_dataframe(self, export_path):
        self.dataframe.to_csv(export_path, index=False)
