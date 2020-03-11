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
    assert join(getcwd(),'temp_file.temp') in temp_codecounter.code_files['.temp']


def test_read_lines_of_code():
    from os import remove
    from codecounter.codecounter import Counter
    with open('fake_code_file.py', 'w') as outfile:
        print("import os\nprint('Hello World')\n", file=outfile)
    temp_counter = Counter('.')
    num_lines = temp_counter.read_lines_of_code('fake_code_file.py')
    remove('fake_code_file.py')
    assert num_lines == 3
