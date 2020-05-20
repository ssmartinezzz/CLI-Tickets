import re

def parse_args(string):
    result = string.split()

    return result


def parseSpaces(string):
    command = []
    aux = str()
    auxiliarArray = str()

    if re.split("\"", string):
        for i in string.split(" "):
            command.append(i)

        for i in command:
            aux = aux + i + " "

        auxiliarArray = [x.strip() for x in re.split(r'(?<!^)(?=\s+-)', aux)]


    return auxiliarArray










