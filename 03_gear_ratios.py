import re

# Puzzle input from https://adventofcode.com/2023/day/3/input
file = open("03_input.txt", "r")
input = file.readlines()

# It was treating the newline character as a 'symbol',
# So let's strip the strings
engineSchematic = []
for line in input:
  engineSchematic.append(line.strip()) 

sumOfPartNumbers = 0

def validateChar(char):
  if char.isdigit() or char == '.':
    return False
  else:
    return True

for lineIndex, line in enumerate(engineSchematic):  
  # charIndex will help me check for duplicate numbers on the same line
  charIndex = 0
  partNumerals = re.findall("\d+", line)
  for partNumeral in partNumerals:
    validPart = False
    # get the index of number in the string
    numeralIndex = line.find(partNumeral, charIndex)
    if numeralIndex == -1:
      print("Didn't find numerals; something's gone wrong")
    # get how long it is
    numeralLength = len(partNumeral)
    
    # check for symbols around it
    #   stay within `engineSchematic` AND `line` bounds
    # How can we check?
    # - check characters one by one
    # - We could also add all of the characters to a string and then check once ... maybe this is dumb

    # To the left
    if numeralIndex > 0 and not validPart:
      char = line[numeralIndex - 1]
      validPart = validateChar(char)
    # To the right
    nextIndex = numeralIndex + numeralLength
    if nextIndex <= len(line) - 1 and not validPart:
      char = line[nextIndex]
      validPart = validateChar(char)
    
    # We need to account for checking within bounds on the upper/lower line
    lineStartIndex = max(numeralIndex - 1, 0)
    lineEndIndex = min(numeralIndex + numeralLength + 1, len(line) - 1)
    # Upper
    if lineIndex > 0 and not validPart:
      checkString = engineSchematic[lineIndex - 1][lineStartIndex : lineEndIndex]
      for char in checkString:
        validPart = validateChar(char)
        if validPart:
          break
    # Lower
    if lineIndex < len(engineSchematic) - 1 and not validPart:
      checkString = engineSchematic[lineIndex + 1][lineStartIndex : lineEndIndex]
      for char in checkString:
        validPart = validateChar(char)
        if validPart:
          break

    # If there is a symbol, add partNumber as int to sumOfPartNumbers
    if validPart:
      sumOfPartNumbers += int(partNumeral)
    # Update `charIndex` so we only search later in the line
    charIndex = numeralIndex + numeralLength
    
print(sumOfPartNumbers)
