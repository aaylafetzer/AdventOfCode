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

if !(ARGV.size == 2)
    puts "Incorrect number of arguments"
    exit()
end

# Get arguments from ARGV
inputDataPath = ARGV[0]
combinationCount = ARGV[1]

# Read file
inputData = File.read_lines(inputDataPath, chomp: true)
# Convert the data to integers
inputData = inputData.map(&.to_i)

# Iterate the possible combinations of the input data until a sum of 2020 is found
inputData.each_combination(combinationCount.to_i) do |combination|
    if combination.sum == 2020
        puts "The combination for n=#{combinationCount} is #{combination} with a product of #{combination.product}"
    end
end