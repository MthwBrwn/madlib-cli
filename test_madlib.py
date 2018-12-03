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


#  need to test input from user

#  need to test list of user answers

#  need to test output of answers and text
#
#
