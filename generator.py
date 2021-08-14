
import random
import string
import math

class Error(Exception):
    """Base class for other exceptions"""
    pass
class InputError(Error):
    """Raised if y or n is not entered"""
    pass


#gets a certain number of numbers
def get_num(times):
    nums = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.digits))
        nums = "".join(temp)
    return nums

#gets certain number of lowercase characters
def get_lower(times):
    lowercase = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.ascii_lowercase))
        lowercase = "".join(temp)
    return lowercase

#gets certain number of uppercase characters
def get_upper(times):
    uppercase = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.ascii_uppercase))
        uppercase = "".join(temp)
    return uppercase

#gets certain number of special characters
def get_special(times):
    specials = ""
    temp = []
    for i in range(times):
        temp.append(random.choice(string.punctuation))
        specials = "".join(temp)
    return specials

#shuffles the password pseudo-randomly
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



size = int(input("What length do you want your password to be? (up to 24 characters)"))


#Try-Except Block for special characters.
while True:
    try:
        special_check = (input("Do you want special characters? (y or n)"))
        if special_check != "y" and special_check != "n":
            raise InputError
        break
    except InputError:
        print("\'y\' or \'n\' not entered")
        print()

if special_check == "y":
    special_check = True
else:
    special_check = False

#Try-Except Block for numbers
while True:
    try:
        num_check = (input("Do you want numbers? (y or n)"))
        if num_check != "y" and num_check != "n":
            raise InputError
        break
    except InputError:
        print("\'y\' or \'n\' not entered")
        print()

if num_check == "y":
    num_check = True
else:
    num_check = False

password = ""
methods = [get_upper, get_lower, get_num, get_special]

#if-elif blocks to address what the user wants
if special_check and num_check:
    dis_size = size/4
    if not float(dis_size).is_integer():
        math.floor(float(dis_size))
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))+(get_special(dis_size))+(get_num(dis_size))
        remainder = size - (dis_size * 4)
        method = random.choice(methods)
        password += method(remainder)
    else:
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))+(get_special(dis_size))+(get_num(dis_size))
        remainder = size - (dis_size * 4)
        method = random.choice(methods)
        password += method(remainder)

elif num_check and not special_check:
    dis_size = size/3
    if not float(dis_size).is_integer():
        math.floor(float(dis_size))
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))+(get_num(dis_size))
        remainder = size - (dis_size * 3)
        method = random.choice(methods)
        password += method(remainder)
    else:
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))+(get_num(dis_size))
        remainder = size - (dis_size * 3)
        method = random.choice(methods)
        password += method(remainder)

elif special_check and not num_check:
    dis_size = size/3
    if not float(dis_size).is_integer():
        math.floor(float(dis_size))
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))+(get_special(dis_size))
        remainder = size - (dis_size * 3)
        method = random.choice(methods)
        password += method(remainder)
    else:
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))+(get_special(dis_size))
        remainder = size - (dis_size * 3)
        method = random.choice(methods)
        password += method(remainder)
elif not special_check and not num_check:
    dis_size = size/2
    if not float(dis_size).is_integer():
        math.floor(float(dis_size))
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))
        remainder = size - (dis_size * 2)
        method = random.choice(methods)
        password += method(remainder)
    else:
        dis_size = int(dis_size)
        password = (get_upper(dis_size))+(get_lower(dis_size))
        remainder = size - (dis_size * 2)
        method = random.choice(methods)
        password += method(remainder)
password = shuffle_word(password)
password = passwordify(password)

# password = (get_upper(2))+(get_lower(2))+(get_special(2))+(get_num(2))
print("Valid password: " + password)
