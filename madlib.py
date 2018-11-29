import json
import re

# need to parse questions and serialize the users questions into a answerlist
def word_open():

    """ word generator
    """
    get_text = open("data.txt", "rt")
    contents = get_text.read()
    get_text.close()
    print(contents)


def greeting():


    print('Hello welcome to our MadLib game.')
    print('You will be asked a series of questions.')
    print('Please reply to each question once prompted.')
    print('Once you are done a MadLib page will be returned to you')
    print ('Lets get started')


# need an out going message stating game and asking questions

def run():

    greeting()
    word_open()


# need to read text back to user with user inputs in place of {questions}

# need to parse info from our data file into a list of strings and then insert
#user input into list at


if __name__ =='__main__':
    run()
