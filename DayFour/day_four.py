import re

passports_file = open("passports.txt", "r")
passports = passports_file.read().split("\n\n")


# Part One

def validatePassport(passports):
    valid_count = 0
    for passport in passports:
        if ("iyr:" in passport and "hcl:" in passport and "pid:" in passport and "eyr:" in passport
                and "byr:" in passport and "hgt:" in passport and "ecl:" in passport):
            valid_count = valid_count + 1
    return valid_count


print("Vaild passports:", validatePassport(passports))


# Part Two

regex_dict = {
    "byr": "(19[2-8][0-9]|199[0-9]|200[0-2])",
    "iyr": "(201[0-9]|2020)",
    "eyr": "(202[0-9]|2030)",
    "hgt": "(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in",
    "hcl": "#[a-f0-9]{6,6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "^[0-9]{9,9}$",
}


def validateValues(passport_dict):
    match_total = 0
    for key in passport_dict:
        if key in regex_dict:
            match = re.findall(regex_dict[key], passport_dict[key])
            if match:
                match_total = match_total + 1
    if match_total == 7:
        return True


def validatePassportValues(passports):
    valid_passport = 0
    for passport in passports:
        passport_dict = dict()
        passport = passport.replace("\n", " ").split(" ")
        for values in passport:
            key, value = values.split(":")
            passport_dict.update({key: value})
        if validateValues(passport_dict):
            valid_passport = valid_passport + 1
    return valid_passport
            

print("Valid passports with correct values:", validatePassportValues(passports))
