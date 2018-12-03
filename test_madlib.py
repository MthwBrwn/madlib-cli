import madlib
import sys


def test_import():
    """ First test to make sure import is valid
    """
    assert True is True


def test_run(capsys):
    """ tests to see if terminal call runs print
    """
    madlib.greeting()
    capt = capsys.readouterr()
    assert capt.out == "Hello welcome to our MadLib game.\nYou will be asked a series of questions.\nPlease reply to each question once prompted.\nOnce you are done a MadLib page will be returned to you\nLets get started\n"

def test_read_file():
    contents = madlib.read_file('./data.txt')
    assert contents.startswith('Make Me A Video Game!')

#  def read_right():
#     """checking to read if read is working"""
#     assert madlib.word_open


#  need to test input from user

#  need to test list of user answers

#  need to test output of answers and text
#
#
