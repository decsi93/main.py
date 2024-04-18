sentences = [" "]

"""def abcd():
    f = open("abcd.txt")
    abc = (f.readlines())
    i = 0
    while i != len(abc):
        abc[i] = abc[i].strip()
        i += 1
    return abc
"""


def in_take():
    userinput = "test.txt"  # input("file name: ")
    source = ""
    flag = True
    try:
        source = open(userinput, encoding="utf-8")
    except FileNotFoundError:
        try:
            userinput += ".txt"
            source = open(userinput, encoding="utf-8")
        except FileNotFoundError:
            flag = False
            print("File not found\nPlease check the file and try again\n")

    if flag:
        global sentences
        sentences.clear()
        for string in source:
            text = string.strip()
            sentences.append(text)
        return sentences


space_counter = 0
capital_counter = 0
punctuation_counter = 0


def punctuation_validator(text: str) -> bool:
    punctuations = [".", "?", "!"]
    global punctuation_counter

    for char in text:
        for punctuation in punctuations:

            if char == punctuation:
                punctuation_counter += 1

    if punctuation_counter == 0 or punctuation_counter > 1:
        return False

    elif punctuation_counter == 1:
        return True


def white_space_validator(text: str) -> bool:
    global space_counter

    for char in text:
        if char.isspace():
            space_counter += 1

    if space_counter < 1:
        return False
    else:
        return True


def capital_validator(text: str) -> bool:
    global capital_counter

    for char in text:
        print(char)
        global capital_counter
        if not char.isnumeric() and not char.isspace():
            if char.isupper():
                capital_counter += 1

    if capital_counter == 0:
        return True
    else:
        return False


def is_ascii(text: str) -> bool:
    try:
        (text.encode(encoding="utf-8")
         .decode(encoding="ascii"))
    except UnicodeDecodeError:
        return False
    else:
        return True


def duplicates(text: str) -> bool:
    words = text.split(" ")
    words[-1] = words[-1].strip(words[-1][-1])

    if len(words) == len(set(words)):
        return True
    else:
        return False


def validation():
    in_take()
    valids = []
    valid_counter = 0
    global space_counter, capital_counter, punctuation_counter

    for sentence in sentences:

        if (punctuation_validator(sentence) and white_space_validator(sentence) and capital_validator(sentence)
                and is_ascii(sentence) and duplicates(sentence)):

            valids.append([sentence, True, space_counter, capital_counter, punctuation_counter])

            valid_counter += 1
            space_counter = 0
            capital_counter = 0
            punctuation_counter = 0

        else:
            valids.append([sentence, False, space_counter, capital_counter, punctuation_counter])

            space_counter = 0
            capital_counter = 0
            punctuation_counter = 0

    return valids, valid_counter


print(validation())
