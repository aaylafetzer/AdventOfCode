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
import math

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
args = parser.parse_args()

# Ensure that the user has provided a real path
assert os.path.exists(args.input)

# Load input data from file
with open(args.input, "r") as inputFile:
    inputData = [int(item) for item in inputFile.readlines()]

def calculateFuel(mass):
    return (math.floor(mass / 3) - 2)

# Preform calculations for required fuel
cargoFuel = 0
for item in inputData:
    moduleFuel = 0
    moduleFuel += calculateFuel(item)
    # Fuel required for the extra fuel
    addition = calculateFuel(calculateFuel(item))
    while addition > 0:
        moduleFuel += addition
        addition = calculateFuel(addition)
        print(f"Adding {addition}")
    cargoFuel += moduleFuel

print(f"Total fuel required is {cargoFuel}")