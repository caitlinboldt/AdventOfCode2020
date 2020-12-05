# How many passwords are valid according to their policies?

import re

# Open file.
passwordFile = open("passwords.txt", "r")


def checkIfValid(password_line):
    range_requirement = re.findall("[0-9]+", password_line)
    low_range = int(range_requirement[0])
    high_range = int(range_requirement[1])
    letter_requirement = " ".join(re.findall(".(?=:)", password_line))
    password = " ".join(re.findall(": (.*)", password_line))
    # Check if the letter requirement is found in the password.
    if letter_requirement in password:
        if password[low_range - 1] == letter_requirement and not password[high_range - 1] == letter_requirement:
            return True
        if password[high_range - 1] == letter_requirement and not password[low_range - 1] == letter_requirement:
            return True


valid_count = 0

# Read each password from the file, check if valid and add to valid password count.
for line in passwordFile:
    password_line = line.strip()
    if checkIfValid(password_line):
        valid_count = valid_count + 1


print("There are {} valid passwords.".format(valid_count))

# Close file.
passwordFile.close()
