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
import re

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
# This is 4 parts. 
# ["3", "4", "v", "vvmv"]
# The first element is the low end of a range, the second element is the high end,
# the third element is the char to search the fourth element (given password) for.

# Define regular expression. Expression adapted from @wundrweapon
# https://github.com/wundrweapon/aoc-2020/blob/master/day2-2.lua
expression = re.compile("^(\d+)-(\d+) (\w): (\w+)$")

valid_passwords_1 = []
valid_passwords_2 = []
for item in inputData:
    low, high, char, pw = expression.findall(item)[0]
    # Convert to int
    low = int(low) - 1
    high = int(high) - 1

    # Part 1
    count = pw.count(char)
    if low <= count <= high:
        valid_passwords_1.append(pw)
    
    # Part 2
    if (pw[low] == char) ^ (pw[high] == pw):
        valid_passwords_2.append(pw)

print(f"There are {len(valid_passwords_1)} valid passwords for Part 1")
print(f"There are {len(valid_passwords_2)} valid passwords for Part 2")
