"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    # open file located at file path
    # read contents of file as one string
    # return that string
    
    words = ""

    file = open(file_path)

    for line in file:
        line = line.strip()
        # print(line)
        words = words + line + " "
        # print(words)
    words = words[0:-1:1]
    
    return words


# open_and_read_file('green-eggs.txt')

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

    # take input string (representing the file contents) and turn it into an
        # list of words) # ["Would", "you", "could", "you",...]
    # iterate through the words 
        # and get a slice of three words

        # add an entry to chains where the key is the tuple containing the first
            # two words, and the value is an array containing whatever
            # it contained before PLUS the third word in the slice
        # we'll do this by checking if the key is already in chains
            # if it is, just add the third word in the slice to the list value
            # if it is not, 
    
    chains = {}
    words_list = text_string.split(" ")
    # print("WORDS_LIST: ", words_list)

    end_index = len(words_list) - 2

    for idx, word in enumerate(words_list):
        if idx == end_index:
            break
        words_slice = words_list[idx:idx+3]
        bigram = (words_slice[0], words_slice[1])
        # feedback: bigram = (words_list[idx], words_list[idx+1])
        print(chains.get(bigram, False))
        if chains.get(bigram, False):
            chains[bigram].append(words_slice[2])
        else:
            chains[bigram] = [words_slice[2]]
        # print(bigram in chains)
    
    print(chains)   
        # print(bigram)
        # print("TEST:", words_slice)

        # print("ENUMERATE:", idx, word)
    

    # chains = {
    #     ('Would', 'you'): ['could', 'could', 'could', 'could', 'like'],
    #     ('you,', 'could'): ['you', 'you', 'you', 'you'],
    #     ('could', 'you'):  ['in', 'with', 'in', 'with'],
    #     ('you', 'in'):     ['a', 'a'],
    #     ('in', 'a'):       ['house?', 'box?'],
    #     # ...
    #     ('Sam', 'I'):      ['am?']
    # }




    # your code goes here

    return chains

text = open_and_read_file('green-eggs.txt')
make_chains(text)
# make_chains(text)

def make_text(chains):
    """Return text from chains."""

    from random import choice
    
    # words = ['cat', 'hat', 'sprinkler']
    words = []
    # print("CHAINS: ", chains)
    # print("TYPE: ", type(chains.keys()), chains.keys())

    # pick a starting point
        # randomly pick a key from chains
        # randomly pick a next word from the value associated with that key
        # together, these three words are our link
    # add link to our words list
    # use the rightmost two words in the words list to figure out what our next
    # key is.
    # using that key, randomly pick a next word from the value associated
    # add this word to the words list.
    # we keep doing this until we are looking for a key that is not in chains.
    # make a string out of the words list

    start = choice(list(chains.keys()))  # tuple
    #iterate
    next_word = choice(chains[start])   # string
    words.append(start[0])
    words.append(start[1])
    words.append(next_word)

    print("START: ", type(start), "NEXT_WORD: ", type(next_word))

    
    return ' '.join(words)



input_path = 'green-eggs.txt'
# input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)


# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print("RANDOM TEXT: ", random_text)



# print(input_text)
# print(range(len(input_text)))