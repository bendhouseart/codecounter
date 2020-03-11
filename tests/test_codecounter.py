#!/usr/bin/env python

"""Tests for `codecounter` package."""

import pytest



@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_pass_bad_directory():
    from codecounter import codecounter
    with pytest.raises(NotADirectoryError):
        codecounter.Counter("Imabaaaaadpath.path.so.bad")


def test_pass_good_directory():
    from codecounter import codecounter
    import os
    good_dir = os.getcwd()
    good_dir_counter_object = codecounter.Counter(good_dir)
    assert type(good_dir_counter_object) is codecounter.Counter


def test_pass_collect_file_extension_file_w_extension():
    from codecounter.codecounter import Counter
    x = Counter('.')
    assert x.collect_file_extension('temp.file') == '.file'


def test_pass_collect_file_extension_file_w_out_extension():
    from codecounter.codecounter import Counter
    x = Counter('.')
    assert x.collect_file_extension('file') == ''


def test_collect_files():
    from codecounter import codecounter
    from os import getcwd, remove
    from os.path import join

    temp_file = open('temp_file.temp', 'w')
    temp_file.close()
    temp_codecounter = codecounter.Counter(getcwd())
    temp_codecounter.collect_files()
    remove('temp_file.temp')
    for index, code_file in enumerate(temp_codecounter.code_files['.temp']):
        if join(getcwd(), 'temp_file.temp') in code_file['File']:
            check_here = index
            break
        else:
            raise FileNotFoundError
    assert join(getcwd(), 'temp_file.temp') in temp_codecounter.code_files['.temp'][check_here]['File']


def test_read_lines_of_code():
    from os import remove
    from codecounter.codecounter import Counter
    with open('fake_code_file.py', 'w') as outfile:
        print("import os\nprint('Hello World')\n", file=outfile)
    temp_counter = Counter('.')
    num_lines = temp_counter.read_lines_of_code('fake_code_file.py')
    remove('fake_code_file.py')
    assert num_lines == 3


def test_collect_column_names_from_build_dataframe():
    import pandas
    from os import remove
    from codecounter.codecounter import Counter
    with open('fake_code_file.py', 'w') as outfile:
        print("import os\nprint('Hello World')\n", file=outfile)
    temp_counter = Counter('.')
    temp_counter.collect_files()
    remove('fake_code_file.py')
    temp_counter.build_dataframe()
    assert list(temp_counter.dataframe.columns) == ['FileType', 'File', 'Number_Of_Lines']


def test_build_dataframe():
    import pandas
    from os import remove
    from codecounter.codecounter import Counter
    with open('fake_code_file.py', 'w') as outfile:
        print("import os\nprint('Hello World')\n", file=outfile)
    temp_counter = Counter('.')
    temp_counter.collect_files()
    remove('fake_code_file.py')
    temp_counter.build_dataframe()
    assert type(temp_counter.dataframe) is pandas.DataFrame
    assert len(temp_counter.dataframe) >= 1


def test_export_dataframe():
    import pandas
    from os import remove, getcwd
    from os.path import join
    from codecounter.codecounter import Counter
    with open('fake_code_file.py', 'w') as outfile:
        print("import os\nprint('Hello World')\n", file=outfile)
    temp_counter = Counter('.')
    temp_counter.collect_files()
    remove('fake_code_file.py')
    temp_counter.build_dataframe()
    temp_counter.export_dataframe(join(getcwd(), 'test_dataframe.csv'))
    # opening up dataframe:
    loaded_df = pandas.read_csv(join(getcwd(), 'test_dataframe.csv'), index_col=False)
    pandas.set_option('display.max_columns', None)
    print(temp_counter.dataframe)
    print(loaded_df)
    assert list(loaded_df.columns) == ['FileType', 'File', 'Number_Of_Lines']
    assert len(loaded_df) >= 1
