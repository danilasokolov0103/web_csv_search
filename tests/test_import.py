
import pytest
import sys
sys.path.append("..")
from file_import.import_csv import import_from_csv
from file_import.find_info import show_info

data = {'Brittney Abrehart': [['6/24/1981', 'Manager']],
        'Odie Lowthian': [['7/19/1994', 'Python Engineer']],
        'Duky Ruttgers': [['8/17/1963', 'Driver']],
        'Geneva Plevin': [['3/4/1952', 'Big boss']],
        'Gabrielle Creigan': [['9/14/1946', 'Waitress']]}


def test_import1():
    assert import_from_csv('test.html') == 'Wrong file type'


def test_import2():
    assert import_from_csv('test.txt') == 'Wrong file type'


def test_import3():
    assert import_from_csv('test.jpg') == 'Wrong file type'


def test_import4():
    assert import_from_csv('test.csv') == data


