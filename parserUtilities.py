import re
"""
This file is the implementation of the re module that allows us to
split, parse strings
"""
def parseargs(string):

    result = string.split()

    return result


def parse_spaces(string):
    """
    This function parses the input string splitting spaces between the
    different commands.
    @param string: Its a string containing the literal command that clients insert
    @return: It returns the commands string splitted in an Array.
    """
    auxiliary_array = []

    for s in string:

        auxiliary_array = ([x.strip() for x in re.split(r'(?<!^)(?=\s+-)',string)])

    return auxiliary_array










