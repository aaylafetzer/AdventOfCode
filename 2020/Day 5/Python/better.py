# @wundrweapon was kind enough to explain to my dumb ass why my answer was bad 
# and how to do it better. Here goes nothing.

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
    inputData = [boardingPass.strip() for boardingPass in inputFile.readlines()]

translations = {
    "F": "0",
    "B": "1",
    "L": "0",
    "R": "1"
}

seatIDList = []
for boardingPass in inputData:
    seatID = int(
        reduce(lambda x, y: x.replace(y, translations[y]), translations, boardingPass)
        , 2)
    seatIDList.append(seatID)
print(f"Maximum Seat ID is {max(seatIDList)}")

# Find my seat
for i in range(max(seatIDList)):
    if i not in seatIDList and i + 1 in seatIDList and i - 1 in seatIDList:
        print(f"My seat is {i}")