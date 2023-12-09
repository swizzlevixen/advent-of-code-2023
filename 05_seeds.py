import re
from collections import namedtuple

# Puzzle input from https://adventofcode.com/2023/day/5/input
file = open("05_example.txt", "r")
input = file.read()

##########
# Input format
# Almanac (see example)
#
# The maps describe ranges of numbers that can be converted.
# Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
# Any source numbers that aren't mapped correspond to the same destination number.
# Convert each seed number through other categories until you can find its corresponding location number
#
# What is the lowest location number that corresponds to any of the initial seed numbers?
# Example: 35
##########

# Load maps
# Hey Rey, some named tuples!
MapPack = namedtuple("MapPack", "destination source length") # Ints
MapRange = namedtuple("MapRange", "destination source") # Ranges

# Find the line with 'seeds:'
# then convert numerals to int list
# seeds = list(map(int, re.findall("\d+", seedsStr)))
seedsStr = re.search(r"^seeds: (.*)\n", input).group(1)
seeds = list(map(int, re.findall("\d+", seedsStr)))

seedToSoilMap = []
seedToSoilLines = re.search(r"seed-to-soil map:\s((.+\n)+)\n", input).group(1).splitlines()
for line in seedToSoilLines:
  mapPack = MapPack(*list(map(int, re.findall("\d+", line))))
  destRange = range(mapPack.destination, mapPack.destination + mapPack.length + 1)
  sourceRange = range(mapPack.source, mapPack.source + mapPack.length + 1)
  mapRange = MapRange(destRange, sourceRange)
  seedToSoilMap.append(mapRange)
# print(seedToSoilMap)

for seed in seeds:
  isMapped = False
  for soilMap in seedToSoilMap:
    if seed in soilMap.source:
      dest = seed - soilMap.source.start + soilMap.destination.start
      isMapped = True
      break
  # FIXME: need to add these back to a conversion list, but for test just print 'em
  if isMapped:
    print(dest)
  else:
    print(seed)

# TODO: Keep converting      
