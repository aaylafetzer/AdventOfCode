import argparse
import os
import math

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
args = parser.parse_args()

# Ensure that the user has provided a real path
assert os.path.exists(args.input)

# Load input data from file
with open(args.input, "r") as inputFile:
    inputData = [boardingPass.strip() for boardingPass in inputFile.readlines()]

codes = {
    "F": lambda x: x[:math.floor(len(x)/2)],
    "B": lambda x: x[math.floor(len(x)/2):],
    "L": lambda x: x[:math.floor(len(x)/2)],
    "R": lambda x: x[math.floor(len(x)/2):]
}

seatIds = []
# Find the row, column for each pass
for boardingPass in inputData:
    # Find the correct row
    rows = list(range(128))
    for char in boardingPass[:7]:
        rows = codes[char](rows)
        # print(f"{char}: Low: {rows[0]}, High: {rows[-1]}")
    row = rows[0]
    # Find the correct column
    columns = list(range(8))
    for char in boardingPass[7:]:
        columns = codes[char](columns)
        # print(f"{char}: Low: {columns[0]}, High: {columns[-1]}")
    column = columns[0]
    # Calculate the Seat ID
    seatID = (row * 8) + column
    seatIds.append(seatID)
    print(f"Row: {row}, Column: {column}, ID: {seatID}")
print(f"Highest ID was {max(seatIds)}")

# Find my seat
seatIds.sort()
for seat in range(max(seatIds)):
    if seat not in seatIds and seat + 1 in seatIds and seat - 1 in seatIds:
        print(f"My seat is {seat}")