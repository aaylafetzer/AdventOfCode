import argparse
import os
import string

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
args = parser.parse_args()

# Ensure that the user has provided a real path
assert os.path.exists(args.input)

# Load input data from file
with open(args.input, "r") as inputFile:
    inputData = inputFile.readlines()
# Deal with the input's bullshit
passports = []
currentPassport = {}
for i in range(len(inputData)):
    if inputData[i] == "\n":
        passports.append(currentPassport)
        currentPassport = {}
    for value in inputData[i].split():
        k, v = value.split(':')
        currentPassport[k] = v
# Count the last passport
passports.append(currentPassport)

# Define a Passport Class
class Passport:
    # Required fields
    # required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    required = {
        "byr": lambda x: (int(x) >= 1920 and int(x) <= 2002),
        "iyr": lambda x: (int(x) >= 2010 and int(x) <= 2020),
        "eyr": lambda x: (int(x) >= 2020 and int(x) <= 2030),
        # I have brough shame upon my family with this lambda
        "hgt": lambda x: (
            len(x) >= 4 and (
                (int(x[:-2]) >= 150 and int(x[:-2]) <= 193) 
                if x[-2:] == "cm" else
                (int(x[:-2]) >= 59 and int(x[:-2]) <= 76)
            )    (int(x[:-2]) >= 150 and int(x[:-2]) <= 193) 
                if x[-2:] == "cm" else
                (int(x[:-2]) >= 59 and int(x[:-2]) <= 76)
        ),
        "hcl": lambda x: (len(x[1:]) == 6 and all(c in string.hexdigits for c in x[1:])),
        "ecl": lambda x: (x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
        "pid": lambda x: (len(x) == 9 and all(c in string.digits for c in x))
    }
    # Define class data from dict
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def isValid(self):
        for requirement in self.required:
            if hasattr(self, requirement):
                print(requirement, end=": ")
                print(getattr(self, requirement))
                if not self.required[requirement](getattr(self, requirement)):
                    return False
            else:
                return False
        return True

# Create the passport objects from the inputs
validPassports = 0
for passport in passports:
    if Passport(passport).isValid():
        validPassports += 1
print(f"There are {validPassports} valid passports")