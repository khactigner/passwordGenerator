# First goal: Make a generator of 8 characters that has a combination of uppercase, numbers, and special characters.
# Second goal:
import random
import string


def get_num(times):
    nums = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.digits))
        nums = "".join(temp)
    return nums


def get_lower(times):
    lowercase = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.ascii_lowercase))
        lowercase = "".join(temp)
    return lowercase


def get_upper(times):
    uppercase = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.ascii_uppercase))
        uppercase = "".join(temp)
    return uppercase


def get_special(times):
    specials = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.punctuation))
        specials = "".join(temp)
    return specials


def shuffle_word(word):
    shuffled = "".join(random.sample(word, len(word)))
    return shuffled


# This makes sure the first character of the password is a alphabetical character.
def passwordify(word):
    special_list = list(string.punctuation)
    contained = [x for x in word if x in special_list]
    is_password = False
    word = list(word)
    for i in contained:
        if word[0] in contained:
            word.remove(i)
            word.append(i)
    print(word)
    return "".join(word)


# password = (get_upper(2)).join(get_lower(2)).join(get_special(2)).join(get_num(2))
# print("Original password: " + password)
# password = shuffle_word(password)
# print("Shuffled password: " + password)
# password = (passwordify(password))
# print("Valid password: " + password)

print(passwordify("!3^cjKCi"))
