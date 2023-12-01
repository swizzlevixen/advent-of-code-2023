# Test values
# lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

# Puzzle input from https://adventofcode.com/2023/day/1/input
file = open("01_input.txt", "r")
lines = file.readlines()

sum = 0

for line in lines:
    digits = list(filter(str.isdigit, line))
    firstDigit = digits[0]
    lastDigit = digits[-1]
    digits = firstDigit + lastDigit
    twoDigitNumber = int(digits)
    sum += twoDigitNumber

print(sum)
