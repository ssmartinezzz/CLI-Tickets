import re

def parse_args(string):
    result = string.split()

    return result


def parseSpaces(string):
    auxiliarArray = []
    for s in string:
        auxiliarArray = ([x.strip() for x in re.split(r'(?<!^)(?=\s+-)',string)])


    return auxiliarArray










