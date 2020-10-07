"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_1 = open(file_path)
    file_text = file_1.read()
    return file_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    text_string_list = text_string.split()

    #parsing through text string using the loop
    for i in range(0, len(text_string_list)):
        #create a tuple of current word and next word 
        # eg: if input string = "Would you could"; output would be: ('Would', 'you,')('you,', 'could')
        if i < len(text_string_list)-1:
            dict_key = (text_string_list[i], text_string_list[i + 1])

            if i < len(text_string_list)-2:
                dict_key_val = [text_string_list[i + 2]]
                chains[dict_key]= chains.get(dict_key, []) + dict_key_val
                 
    return chains


def make_text(chains):
    """Return text from chains."""

    # Randomly select a dictionary key from chains
    keys_list = list(chains.keys())
    current_key = choice(keys_list)
    words = [current_key[0], current_key[1]]

    def generate_rand_current_word(chains, current_key):
        dict_value_of_current_key= chains[current_key]
        rand_current_word = choice(dict_value_of_current_key)
        return rand_current_word
    
    words.append(generate_rand_current_word(chains, current_key))
    current_key = (words[1], words[2])

    # Main function program
    while current_key in chains:
        words.append(generate_rand_current_word(chains, current_key))
        len_words = len(words)
        current_key = (words[len_words-2], words[len_words-1])

    return ' '.join(words) 
    
input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
