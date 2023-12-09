import re

# Puzzle input from https://adventofcode.com/2023/day/4/input
file = open("04_input.txt", "r")
input = file.readlines()

##########
# Part 2
# 
# Input format
# Card n: n n n ... | n n n ...
# Where `n n n ...` are arranged: winning numbers | your numbers
#
# Figure out which of the numbers you have appear in the list of winning numbers. 
# 
# There's no such thing as "points". Instead, scratchcards only cause you to 
# win more scratchcards equal to the number of winning numbers you have.
#
# Copies of scratchcards are scored like normal scratchcards
# and have the same card number as the card they copied.
# (Cards will never make you copy a card past the end of the table.)
#
# Process all of the original and copied scratchcards until no more scratchcards
# are won. Including the original set of scratchcards,
#  how many total scratchcards do you end up with?
##########

totalCards = 0

cards = []

print("Converting input...")
for line in input:
  winningStr, yourStr = line.strip('\n').split('|')
  # Get rid of the card number
  winningStr = winningStr.split(':')[1]
  # I'm going to assume that the cards are all numbered sequentially
  winningInts = list(map(int, re.findall("\d+", winningStr)))
  yourInts = list(map(int, re.findall("\d+", yourStr)))
  card = (winningInts, yourInts)
  cards.append(card)

def processCard(index, card):
  global totalCards
  totalCards += 1
  matches = len(set(card[0]) & set(card[1]))
  # print(f"Card {index + 1} has {matches} matches")
  if matches > 0:
    for offset in range(1, matches + 1):
      cardIndex = index + offset
      processCard(cardIndex, cards[cardIndex])

print("Processing...")
for index, card in enumerate(cards):
  # Don't forget that the card number is off-by-one of the list index
  # EXCEPT that as long as they're in order, it really doesn't matter ...?
  processCard(index, card)
  
print(f"Total cards: {totalCards}")
