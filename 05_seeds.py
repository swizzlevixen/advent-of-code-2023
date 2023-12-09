import re
from collections import namedtuple
from typing import List

# Puzzle input from https://adventofcode.com/2023/day/5/input
file = open("05_input.txt", "r")
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

# Named tuples for maps
MapPack = namedtuple("MapPack", "destination source length") # Ints
MapRange = namedtuple("MapRange", "destination source") # Ranges

def extractMap(mapName: str, input: str) -> List[str]:
  """Takes the input string and searches for the map name provided
  Returns a list of lines (str) below that title until the next blank line
  """
  searchString = f"{mapName}\s((.+\n)+)\n"
  mapLines = re.search(searchString, input).group(1).splitlines()
  return mapLines

def parseMap(mapLines: List[str]) -> List[MapRange]:
  """ Convert a list of numerical strings into a list of mapped ranges
  """
  rangeMap = []
  for line in mapLines:
    mapPack = MapPack(*list(map(int, re.findall("\d+", line))))
    destRange = range(mapPack.destination, mapPack.destination + mapPack.length + 1)
    sourceRange = range(mapPack.source, mapPack.source + mapPack.length + 1)
    mapRange = MapRange(destRange, sourceRange)
    rangeMap.append(mapRange)
  return rangeMap

def mapValues(sourceList: List[int], mapRanges: List[MapRange]) -> List[int]:
  """ Uses mapped ranges to convert a list of ints to another list
  """
  destList = []
  for source in sourceList:
    # destination defaults to source if no map
    dest = source
    for mapRange in mapRanges:
      if source in mapRange.source:
        dest = source - mapRange.source.start + mapRange.destination.start
        break # We don't need to keep searching
    destList.append(dest)
  return destList

def loadSeeds(input: str) -> List[int]:
  # Find the line with 'seeds:' then convert numerals to int list
  seedsStr = re.search(r"^seeds: (.*)\n", input).group(1)
  seeds = list(map(int, re.findall("\d+", seedsStr)))
  print("seeds:", seeds)
  return seeds

def processMap(source: List[int], mapName: str, input: str) -> List[int]:
  """Extract the map below the string mapName from the input, 
  and then convert the source values through that map
  """
  mapLines = extractMap(mapName, input)
  theMap = parseMap(mapLines)
  destination = mapValues(source, theMap)
  print(mapName, destination)
  return destination

if __name__ == '__main__':
  seeds = loadSeeds(input)
  soils = processMap(seeds, "seed-to-soil map:", input)
  fertilizers = processMap(soils, "soil-to-fertilizer map:", input)
  waters = processMap(fertilizers, "fertilizer-to-water map:", input)
  lights = processMap(waters, "water-to-light map:", input)
  temps = processMap(lights, "light-to-temperature map:", input)
  humids = processMap(temps, "temperature-to-humidity map:", input)
  locations = processMap(humids, "humidity-to-location map:", input)
  print("smallest location:", min(locations))
