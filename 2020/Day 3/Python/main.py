import argparse
import os

# Define the starting position
startx = 0
starty = 0

# Take the path to the puzzle input as an argument
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Puzzle Input")
parser.add_argument("-x", help="X Slope", default=3, type=int)
parser.add_argument("-y", help="Y Slope", default=1, type=int)
parser.add_argument("--notrees", help="Don't print trees", action="store_true")
args = parser.parse_args()

# Define the slope
rise = args.y
run = args.x

# Ensure that the user has provided a real path
assert os.path.exists(args.input)

# Load input data from file
with open(args.input, "r") as inputFile:
    inputData = [[char for char in line.strip()] for line in inputFile.readlines()]

# Implement Y slope
slope = []
for i in range(len(inputData)):
    if i % rise == 0:
        slope.append(inputData[i])

# Take the starting position
x = startx
trees = 0
# Traverse the slope
for part in slope:
    if not args.notrees:
        print(''.join(part), end=" " * 10)
    if x > len(part) - 1:
        x %= len(part)
    # print(x)
    if part[x] == "#":
        # Position is a tree
        trees += 1
        part[x] = "X"
    else:
        pass
        part[x] = "O"
    if not args.notrees:
        print(''.join(part))
    x += run

print(trees)

# print(inputData)