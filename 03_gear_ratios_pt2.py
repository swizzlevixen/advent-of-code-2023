import re

# Part 2
#
# A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.
#
# What is the sum of all of the gear ratios in your engine schematic?


# Puzzle input from https://adventofcode.com/2023/day/3/input
file = open("03_input.txt", "r")
input = file.readlines()

# It was treating the newline character as a 'symbol',
# So let's strip everything'
engineSchematic = []
for line in input:
  engineSchematic.append(line.strip())
  
# This is a total hack, but if I search for the `*` gears first,
#   then I can more easily calculate if each number is next to one?
#   instead of starting from the gears and crawling out to the numbers from there
#   uggggh this sounds terrible, but let's try it
class Gear (object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.adjacentParts = []
    
  def __str__(self):
    return f"{self.x}, {self.y}, {self.adjacentParts}"
    
class GearsList (list):
  def __str__(self):
    returnString = '[\n'
    for gear in self:
      returnString += f"  {{x: {gear.x}, y: {gear.y}, adjacentParts: {gear.adjacentParts}}},\n"
    returnString += ']'
    return returnString
      
  def addPartToGear(self, x, y, partNumber):
    # yes, I know the ordering of these arguments is terrible
    gearFound = False
    for gear in self:
      if x == gear.x and y == gear.y:
        gear.adjacentParts.append(partNumber)
        gearFound = True
        print(f"Gear exists at {x}, {y}; appending part {partNumber}")
        break
    if not gearFound:
      print(f"Adding gear at {x}, {y}; appending part {partNumber}")
      newGear = Gear(x, y)
      newGear.adjacentParts.append(partNumber)
      self.append(newGear)
  
  def addGear(self, x, y):
    gearFound = False
    for gear in self:
      if x == gear.x and y == gear.y:
        gearFound = True
        print(f"Gear at {x}, {y} already exists")
        break
    if not gearFound:
      newGear = Gear(x, y)
      self.append(newGear)
    
gears = GearsList()

for lineIndex, line in enumerate(engineSchematic):
  # charIndex will help me check for duplicate numbers on the same line
  charIndex = 0
  partNumerals = re.findall("\d+", line)
  # do I need to check if any of these are duplicates?
  for partNumeral in partNumerals:
    # get the index of number in the string
    numeralIndex = line.find(partNumeral, charIndex)
    if numeralIndex == -1:
      print("Didn't find numerals; something's gone wrong")
    # get how long it is
    numeralLength = len(partNumeral)
    
    # check for symbols around it
    #   stay within `engineSchematic` AND `line` bounds
    
    # To the left
    if numeralIndex > 0:
      char = line[numeralIndex - 1]
      if char == '*':
        gears.addPartToGear(numeralIndex - 1, lineIndex, int(partNumeral))
        
    # To the right
    nextIndex = numeralIndex + numeralLength
    if nextIndex <= len(line) - 1:
      char = line[nextIndex]
      if char == '*':
        gears.addPartToGear(nextIndex, lineIndex, int(partNumeral))
    
    # We need to account for checking within bounds on the upper/lower line
    lineStartIndex = max(numeralIndex - 1, 0)
    lineEndIndex = min(numeralIndex + numeralLength + 1, len(line) - 1)
    # Upper
    if lineIndex > 0:
      checkString = engineSchematic[lineIndex - 1][lineStartIndex : lineEndIndex]
      for subIndex, char in enumerate(checkString):
        if char == '*':
          gears.addPartToGear(lineStartIndex + subIndex, lineIndex - 1, int(partNumeral))
          
    # Lower
    if lineIndex < len(engineSchematic) - 1:
      checkString = engineSchematic[lineIndex + 1][lineStartIndex : lineEndIndex]
      for subIndex, char in enumerate(checkString):
        if char == '*':
          gears.addPartToGear(lineStartIndex + subIndex, lineIndex + 1, int(partNumeral))
          
    # Update `charIndex` so we only search later in the line
    charIndex = numeralIndex + numeralLength
    
print(f"gears:\n{gears}")

sumOfGearRatios = 0
for gear in gears:
  if len(gear.adjacentParts) == 2:
    sumOfGearRatios += gear.adjacentParts[0] * gear.adjacentParts[1]

print(sumOfGearRatios)
