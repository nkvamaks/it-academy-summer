"""
Words.

Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
"""
input_string = """Peter Piper picked a peck of pickled peppers;
A peck of pickled peppers Peter Piper picked;
If Peter Piper picked a peck of pickled peppers,
Where’s the peck of pickled peppers Peter Piper picked?"""

num_different_words = len(set(input_string.split()))
print("The following text:\n\n{}\n\nhas {} different words"
      "".format(input_string, num_different_words))
