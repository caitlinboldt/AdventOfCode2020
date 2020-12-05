import re

passports_file = open("passports.txt", "r")

passports = passports_file.read().split("\n\n")


def validatePassport(passports):
    valid_count = 0
    for passport in passports:
        if "iyr:" in passport and "hcl:" in passport and "pid:" in passport and "eyr:" in passport and "byr:" in passport and "hgt:" in passport and "ecl:" in passport:
            valid_count = valid_count + 1
    return valid_count


print("Vaild passports:", validatePassport(passports))
