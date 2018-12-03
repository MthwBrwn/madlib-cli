
word_list = []
contents = ''

# need to parse questions and serialize the users questions into a answerlist


def read_file(raw):

    """ This function pulls raw data in from the data.txt file
    """
    # with open("./data.txt", "rt")
    with open(raw) as f:
        return f.read()


# need to take contents and parse out {} to be prompts for user

def build_list():
    """
    this function with find the {and } characters in the .txt file
    it uses a first and second variable to iterate through each set
    these are stored as a list """
    second = 0
    num_brackets = contents.count('{')
    for i in range(num_brackets):
        first = contents.find('{', second)
        second = contents.find('}', first)
        found_word = contents[first:second]
        print (found_word)
        word_list.append(found_word)

    return (word_list)

# once a list of found_words is worked out with the slices
# these need to be prompted to user and then the user answer can be swapped with the
# slices and then this list can be set through format.


def greeting():
    """the greeting sets up the game and explains how user should enter words"""
    print ('Hello welcome to our MadLib game.')
    print ('You will be asked a series of questions.')
    print ('Please reply to each question once prompted.')
    print ('Once you are done a MadLib page will be returned to you')
    print ('Lets get started')


# need an out going message stating game and asking questions

def run():
    """ run controls the call stack for the game"""
    greeting()
    # while True:
        # build_list()

# need to read text back to user with user inputs in place of {questions}

# need to parse info from our data file into a list of strings and then insert
# user input into list at


if __name__ == '__main__':
    run()
