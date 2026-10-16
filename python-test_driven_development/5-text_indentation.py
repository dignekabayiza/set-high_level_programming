#!/usr/bin/python3
"""5-text_indentation module.

Prints a text with 2 new lines after each of the characters . ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    i = 0
    while i < len(text):
        line += text[i]
        if text[i] in ".?:":
            print(line.strip(), end="\n\n")
            line = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(line.strip(), end="")
