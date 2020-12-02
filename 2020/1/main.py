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
import itertools
import numpy as np

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
parser.add_argument("-n", help="Number of input numbers that sum to 2020", default=2, type=int)
args = parser.parse_args()

# Ensure that the user has provided a real path
assert os.path.exists(args.input)
# Assert there's actually something to do
assert args.n >= 2

with open(args.input, "r") as inputFile:
    # Read puzzle input from file
    inputData = [int(item.strip()) for item in inputFile.readlines()]

# Part 1 Solution
# Find the combination that sums to 2020.
if args.n == 2:
    for item in inputData:
        if (2020 - item) in inputData:
            print(f"The two numbers are {item} and {(2020 - item)}")
            print(f"The product of the two numbers is {item * (2020 - item)}")
            break

# Part 2 Solution (very bad, but I don't have the math capabilities to make something better)
# Create an iterator of every unique input combination of length n
if args.n > 2:
    inputCombinations = itertools.combinations(inputData, args.n)
    # Find 2020 by iterating
    for combination in inputCombinations:
        if sum(combination) == 2020:
            print(f"The combination for 2020 with n={args.n} is {combination}")
            print(f"The product of {combination} is {np.product(combination)}")