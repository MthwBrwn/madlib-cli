import re
import sys

# need to parse questions and serialize the users questions into a answerlist


def read_file(raw):
    """ This function pulls raw data in from the data.txt file
    """
    # with open("./data.txt", "rt")
    with open(raw) as f:
        return f.read()


def write_file(path, contents):
    """ function to write to file"""
    with open(path, 'w') as wf:
        wf.write(contents)


# need to take contents and parse out {} to be prompts for user
def build_keys(contents):
    """ this method will find the {} characters in the .txt file
    it uses a first and second variable to iterate through each set
    these are stored as a list """
    word_list = list()
    second = 0
    num_brackets = contents.count('{')
    for i in range(num_brackets):
        first = contents.find('{', second) + 1
        second = contents.find('}', first)
        found_word = contents[first:second]
        word_list.append(found_word)
    return (word_list)


def build_stripped(contents):
    """This removes the keys from the raw txt leaving a stripped text """
    regex = r"\{.*?\}"
    output = re.sub(regex, '{}', contents)
    return output


def parse(raw):
    """ parse pulls together tow functions: build keys and build stripped """
    prompts = build_keys(raw)
    stripped = build_stripped(raw)
    return prompts, stripped


def add_response(prompt, responses):
    response = input(f'Please enter a {prompt}: ')
    if response == "quit" or response == "Quit":
        sys.exit()
    responses.append(response)


def get_input_frm_user(prompts):
    responses = []
    for prompt in prompts:
        add_response(prompt, responses)

    return responses


# def greeting():
#     print(dedent("""
#     Hello. Welcome to our MadLib game.\n
#     You will be asked a series of questions.\n
#     Please reply to each question once prompted.\n
#     Once you are done a MadLib page will be returned to you\n
#     Lets get started\n
#     If at any time you would like to quit type "quit".
#     """))

def greeting():
    """the greeting sets up the game and explains how user should enter words"""
    print('Hello. Welcome to our MadLib game.')
    print('You will be asked a series of questions.')
    print('Please reply to each question once prompted.')
    print('Once you are done a MadLib page will be returned to you')
    print('Lets get started')
    print("If at any time you would like to quit type 'quit'.")


def weave_story(raw):
    """ This method handles all of the
    """
    greeting()
    prompts, stripped = parse(raw)
    responses = get_input_frm_user(prompts)
    story = stripped.format(*responses)
    print(story)
    return(story)


def run():
    """ run controls the call stack for the game"""
    raw = read_file('./data.txt')
    story = weave_story(raw)
    write_file('./complete_madlib.txt', story)


if __name__ == '__main__':
    run()
