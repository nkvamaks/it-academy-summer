"""Homework 2."""
import sys


def tongues():
    """Exercise 1: Tongues.

    https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8
    Gandalf's writings have long been available for study, but no one has yet
    figured out what language they are written in. Recently, due to programming
    work by a hacker known only by the code name ROT13, it has been discovered
    that Gandalf used nothing but a simple letter substitution scheme, and
    further, that it is its own inverse|the same operation scrambles the message
    as unscrambles it.

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
    The function will be passed a string for the function to decode. Each string
    will contain up to 100 characters, representing some text written by
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


"""Exercise 3: Valid Parentheses.

https://www.codewars.com/kata/52774a314c2333f0a7000688
Write a function called that takes a string of parentheses, and determines if
the order of the parentheses is valid. The function should return true if the
string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid
ASCII characters. Furthermore, the input string may be empty and/or not contain
any parentheses at all. Do not treat other forms of brackets as parentheses
(e.g. [], {}, <>).
"""


if __name__ == '__main__':
    # Run 'selector' of exercises
    sel = {'1': tongues, '2': jumbled_string, 'Q': sys.exit, 'q': sys.exit}
    while True:
        try:
            exercise_num = input('Input an Exercise Number (1-2) to Execute,'
                                 ' Q/q - to Exit: ')
            print(sel[exercise_num]())
        except KeyError:
            print('Enter the Valid Number of Exercise!')
