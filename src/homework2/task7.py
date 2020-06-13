"""Homework 2."""
import sys


def tongues():
    """Exercise 1: Tongues.

    https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8
    Gandalf's writings have long been available for study, but no one has yet
    figured out what language they are written in. Recently, due to programming
    work by a hacker known only by the code name ROT13, it has been discovered
    that Gandalf used nothing but a simple letter substitution scheme, and
    further, that it is its own inverse|the same operation scrambles the
    message as unscrambles it.

    This operation is performed by replacing vowels in the sequence
    'a' 'i' 'y' 'e' 'o' 'u' with the vowel three advanced, cyclicly, while
    preserving case (i.e., lower or upper).

    Similarly, consonants are replaced from the sequence
    'b' 'k' 'x' 'z' 'n' 'h' 'd' 'c' 'w' 'g' 'p' 'v' 'j' 'q' 't' 's' 'r' 'l'
    'm' 'f' by advancing ten letters.

    So for instance the phrase 'One ring to rule them all.' translates to
    'Ita dotf ni dyca nsaw ecc.'

    The fascinating thing about this transformation is that the resulting
    language yields pronounceable words. For this problem, you will write code
    to translate Gandalf's manuscripts into plain text.

    Your job is to write a function that decodes Gandalf's writings.

    #Input
    The function will be passed a string for the function to decode. Each
    string will contain up to 100 characters, representing some text written by
    Gandalf. All characters will be plain ASCII, in the range space (32) to
    tilde (126).

    #Output
    For each string passed to the decode function return its translation.

    :param str_: string with Gandalf's writings.
    :return: decoded string.
    """
    # Make a dict with translations
    inseq = 'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF'
    outseq = 'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG'

    # Enter Gandalf's text from console
    print("Exercise 1: Gandalf's writings")
    # str_ = 'Ita dotf ni dyca nsaw ecc.'  # simple sample
    str_ = input('I was talking aloud to myself: ')
    transdict = str_.maketrans(inseq, outseq)
    return str_.translate(transdict)  # Return translated string.


def jumbled_string():
    """Exercise 2: String -> N iterations -> String.

    We have a string s
    We have a number n
    Here is a function that takes your string, concatenates the even-indexed
    chars to the front, odd-indexed chars to the back.

    The Task:
    return the result of the string after applying the function to it n times.

    Example where s = "qwertyuio" and n = 2:
    after 1 iteration  s = "qetuowryi"
    after 2 iterations s = "qtorieuwy"
    return "qtorieuwy"

    :param s: string to transform.
    :param n: int, how many times to repeat the transformation.
    :return: transformed string.
    """
    print("Exercise 2: One-two-three - trAnsphOOOrm!")
    # str_ = 'Ita dotf ni dyca nsaw ecc.'  # simple sample
    s = input('Type any string you want to transform: ')
    n = int(input('How many times would you like to do that? '))
    for count_ in range(n):  # transform the string
        s = s[::2] + s[1::2]
    return ''.join(s)


def valid_parentheses():
    """Exercise 3: Valid Parentheses.

    https://www.codewars.com/kata/52774a314c2333f0a7000688
    Write a function called that takes a string of parentheses, and determines
    if the order of the parentheses is valid. The function should return true
    if the string is valid, and false if it's invalid.

    Examples
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true

    Constraints
    0 <= input.length <= 100

    Along with opening (() and closing ()) parenthesis, input may contain any
    valid ASCII characters. Furthermore, the input string may be empty and/or
    not contain any parentheses at all. Do not treat other forms of brackets
    as parentheses (e.g. [], {}, <>).
    """
    print("Exercise 3: Valid Parentheses.")
    str_ = input("Enter a String with Parentheses '()': ")
    parenth = '()'  # for entry check
    stack = []  # stack where parentheses will be saved
    string_par = ''  # new string with just parentheses
    for char in str_:  # get rid of junk and leave just parentheses
        if char in parenth:
            string_par += char
    # general case
    for par in string_par:
        if par == '(':  # add any '(' in stack
            stack.append(par)
        elif stack:  # otherwise remove last '(' from stack
            stack.pop(-1)  # if stack is not empty
        else:  # case when string contains more ')' then '('
            return False
    if stack:  # case when string contains more '(' then ')'
        return False
    else:
        return True  # case with a right parentheses or string w/o parentheses


def hex_string_to_RGB():
    """Exercise 4: Convert A Hex String To RGB.

    https://www.codewars.com/kata/5282b48bb70058e4c4000fa7
    When working with color values it can sometimes be useful to extract the
    individual red, green, and blue (RGB) component values for a color.
    Implement a function that meets these requirements:

    Accepts a case-insensitive hexadecimal color string as its parameter
    (ex. "#FF9933" or "#ff9933")
    Returns an object with the structure {r: 255, g: 153, b: 51} where r, g,
    and b range from 0 through 255

    Note: your implementation does not need to support the shorthand form of
    hexadecimal notation (ie "#FFF")

    Example:
    "#FF9933" --> {r: 255, g: 153, b: 51}
    """
    import re

    print("Exercise 4: Convert A Hex String To RGB.")
    str_ = input("Enter a hexadecimal color string with a following format"
                 " (e.g. #FF0056): ")
    if re.match(r'#[0-9a-fA-F]{6}', str_):
        r = str_[1:3]
        g = str_[3:5]
        b = str_[5:7]
        return {'r': int(r, 16), 'g': int(g, 16), 'b': int(b, 16)}
    else:
        return "Entered string doesn't match the required format!"


if __name__ == '__main__':
    # Run 'selector' of exercises
    sel = {'1': tongues, '2': jumbled_string, '3': valid_parentheses,
           '4': hex_string_to_RGB, 'Q': sys.exit, 'q': sys.exit}
    while True:
        try:
            exercise_num = input('Input an Exercise Number (1-4) to Execute,'
                                 ' Q/q - to Quit: ')
            print(sel[exercise_num]())
        except KeyError:
            print('Enter the Valid Number of Exercise!')
