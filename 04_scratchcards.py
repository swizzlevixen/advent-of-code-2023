import re

# Puzzle input from https://adventofcode.com/2023/day/4/input
file = open("04_input.txt", "r")
input = file.readlines()

##########
# Input format
# Card n: n n n ... | n n n ...
# Where `n n n ...` are arranged: winning numbers | your numbers
#
# Figure out which of the numbers you have appear in the list of winning numbers. 
# The first match makes the card worth one point and each match after the first 
# doubles the point value of that card.
#
# How many points are they worth in total?
##########

totalPoints = 0

for line in input:
  winningStr, yourStr = line.strip('\n').split('|')
  # Get rid of the card number
  winningStr = winningStr.split(':')[1]
  winningInts = list(map(int, re.findall("\d+", winningStr)))
  yourInts = list(map(int, re.findall("\d+", yourStr)))
  
  matches = len(set(winningInts) & set(yourInts))
  # print(f"matches: {matches}")
  if matches > 0:
    cardPoints = 2 ** (matches - 1)
    # print(f"cardPoints: {cardPoints}")
    totalPoints += cardPoints
    
print(f"totalPoints: {totalPoints}")
