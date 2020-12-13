import argparse
import os
from functools import reduce

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
args = parser.parse_args()

# Ensure that the user has provided a real path
assert os.path.exists(args.input)

# Load input data from file
with open(args.input, "r") as inputFile:
    inputData = inputFile.readlines()

# Process unique answers
allAnswers = []
currentAnswers = []
# Collect all the unique chars
for line in inputData:
    if line == "\n":
        allAnswers.append(currentAnswers)
        currentAnswers = []
        continue
    for char in [char for char in line]:
        if char not in currentAnswers and char != "\n":
            currentAnswers.append(char)
allAnswers.append(currentAnswers)

answerSum = sum([len(group) for group in allAnswers])
print(f"Part 1 Answer: {answerSum}")
