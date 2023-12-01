# Test values
# Part A:
# lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
# Part B:
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

# This is extremely dumb, but we are supposed to parse BOTH numbers
#   if they overlap, so this keeps any overlap part
#   while preventing it from matching again
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
for name, digit in englishDigits.items():
    lines = [line.replace(name, digit) for line in lines]

sum = 0

for line in lines:
    digits = list(filter(str.isdigit, line))
    firstDigit = digits[0]
    lastDigit = digits[-1]
    digits = firstDigit + lastDigit
    twoDigitNumber = int(digits)
    sum += twoDigitNumber

print(sum)
