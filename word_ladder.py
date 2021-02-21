#!/in/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony',
    'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots',
    'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    # Create a stack
    stack = []
    # Push the start word onto the stack
    stack.append(start_word)
    # Create a queue
    q = deque()
    # Enqueue the stack onto the queue
    q.append(stack)
    # covering exceptions in the pytest
    if start_word == end_word:
        return stack
    # importing the dictionary
    with open(dictionary_file) as f:
        words = f.readlines()
    # stripping the '/n'
    new_dict = {}
    for i, word in enumerate(words):
        new_dict[i] = word[:-1]
    while len(q) != 0:
        focus_stack = q.popleft()
        for key, word in list(new_dict.items()):
            if _adjacent(focus_stack[-1], word):
                if word == end_word:
                    focus_stack.append(word)
                    return focus_stack
                new_stack = copy.copy(focus_stack)
                new_stack.append(word)
                q.append(new_stack)
                del new_dict[key]
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    # checking for empty inputs
    length = len(ladder)
    if length == 0:
        return False

    for i in range(0, length-1):
        if _adjacent(ladder[i], ladder[i+1]):
                continue
        else:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    # checking for false inputs
    if len(word1) != len(word2):
        return False
    # counting characters
    flag = 0
    # iterating over lists of letters
    lord1 = list(word1.lower())
    lord2 = list(word2.lower())
    for i, letter in enumerate(lord1):
        if letter != lord2[i]:
            flag += 1
    if flag != 1:
        return False
    else:
        return True
