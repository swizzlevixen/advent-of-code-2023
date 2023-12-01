# Test values
# lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
# lines = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]

# Puzzle input from https://adventofcode.com/2023/day/1/input
file = open("01_input.txt", "r")
lines = file.readlines()

# This is extremely dumb, but we are supposed to parse BOTH numbers if they
#   overlap, so this keeps the overlap part while clearning the subbed one
englishDigits = {
    "one": "on1ne",
    "two": "tw2wo",
    "three": "thre3hree",
    "four": "fou4our",
    "five": "fiv5ive",
    "six": "si6ix",
    "seven": "seve7even",
    "eight": "eigh8ight",
    "nine": "nin9ine",
}

# Substitute text names for digits
#   uggghhhh it has overlaps in the text and you have to sub the first one
#   so this doesn't work:
# for name, digit in englishDigits.items():
# lines = [line.replace(name, digit) for line in lines]


def translateDigits(line: str) -> str:
    # Set the marker past the end, so that we can move it backwards,
    # if a match is found
    marker = len(line)
    print(f"line: {line}")
    match = ""

    for name in englishDigits:
        tempMarker = line.find(name)
        if tempMarker > -1 and tempMarker < marker:
            marker = tempMarker
            match = name
    if marker < len(line) and match != "":
        print(f"marker: {marker}, match: {match}")
        # We found something; replace ONLY the first occurrence
        line = line.replace(match, englishDigits[match], 1)
        # Check again, recursively
        line = translateDigits(line)
    return line


sum = 0

for line in lines:
    line = translateDigits(line)
    digits = list(filter(str.isdigit, line))
    firstDigit = digits[0]
    lastDigit = digits[-1]
    digits = firstDigit + lastDigit
    twoDigitNumber = int(digits)
    sum += twoDigitNumber

print(sum)
