""" """
import madlib
import sys


def test_import():
    """ First test to make sure import is valid
    """
    assert True is True


def test_run(capsys):
    """ tests to see if terminal call runs print"""
    madlib.greeting()
    capt = capsys.readouterr()
    assert capt.out == "Hello welcome to our MadLib game.\nYou will be asked a series of questions.\nPlease reply to each question once prompted.\nOnce you are done a MadLib page will be returned to you\nLets get started\n"


def test_read_file():
    """testing if read_file patway works"""
    contents = madlib.read_file('./data.txt')
    assert contents.startswith('Make Me A Video Game!')


def test_writing_right():
    """checking if write_file is  working"""
    contents = 'sample'
    path = './foo.txt'
    madlib.write_file(path, contents)
    with open(path) as f:
        assert f.read() == contents


def test_word_parse():
    """test function to parse keys to user from rax text file """
    keys, stripped = madlib.parse("This is an {adjective} and also {adjective} {noun} of a test.")
    assert keys == ['adjective', 'adjective', 'noun']
    assert stripped == 'This is an {} and also {} {} of a test.'


