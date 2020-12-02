# Copyright (C) 2020 Aayla Fetzer
# 
# This file is part of AdventOfCode.
# 
# AdventOfCode is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# AdventOfCode is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with AdventOfCode.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
args = parser.parse_args()

# Ensure that the user has provided a real path
assert os.path.exists(args.input)

# Load input data from file
with open(args.input, "r") as inputFile:
    inputData = inputFile.readlines()

# A sample password is:
# 3-4 v: vvmv
# This is 3 parts, space-separated. 
# ["3-4", "v:", "vvmv"]
# The first element is a range, the second element is the char that needs
# to be in that range, and the third is the password itself.

# Split the inputs into their 3 parts
inputs = [item.split() for item in inputData]
for i in range(len(inputs)):
    # Split the first part
    inputs[i][0] = inputs[i][0].split("-")
    # Strip the colon from the second part
    inputs[i][1] = inputs[i][1][:-1]


# Part 1, Terrible
valid = [
    item for item in inputs if 
        (item[2].count(item[1]) >= int(item[0][0]) and item[2].count(item[1]) <= int(item[0][1]))
    ]
print(f"There are {len(valid)} valid passwords for Part 1")


# Part 2, Not as bad as Part 1, but still terrible
valid = []
for item in inputs:
    passing = False
    for pos in item[0]: # For each position to test
        if item[2][int(pos) - 1] == item[1]: # Test the position
            if passing == False: # If the input was not yet passing, it is now
                passing = True
            else: # If the input was already passing, but both positions contain the letter, it fails and breaks
                passing = False
                break
    if passing == True: # If the input is still passing, add it to the list of valid passwords
        valid.append(item)
print(f"There are {len(valid)} valid passwords for Part 2")