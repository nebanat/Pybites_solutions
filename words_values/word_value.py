from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    word_list = []
    with open('words_values/{}'.format(DICTIONARY)) as file:
        content = file.readlines()
        for word in content:
            word_list.append(word.strip())
        return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_list = load_words()

    word_lower = word.lower()
    word_proper = word.title()

    if word_lower in word_list:
        word_values = [LETTER_SCORES[character] for character in word.upper()]
    elif word_proper in word_list:
        word_values = [LETTER_SCORES[character] for character in word.upper()]
    else:
        word_values = [LETTER_SCORES[character] for character in word.upper()]
    return sum(word_values)


def max_word_value(list_of_word=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_dict = dict()
    if list_of_word:
        for word in list(list_of_word):
            word_dict.update({word: calc_word_value(word)})
        return max(word_dict, key=lambda key: word_dict[key])
    return 'benzalphenylhydrazone'

