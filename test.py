punctuation_counter = 0


def punctuation_validator(text: str):
    punctuations = [".", "?", "!"]
    global punctuation_counter

    for char in text:
        for punctuation in punctuations:
            if char == punctuation:
                punctuation_counter += 1
                if punctuation_counter >= 2 or punctuation_counter < 1:
                    return False

    if punctuation_counter == 0:
        return False
    elif punctuation_counter == 1:
        return True


a = punctuation_validator("hi!")
print(a)
