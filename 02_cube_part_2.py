## Part 2
##
## The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.
## 
## For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
##

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

import re

#gamesLines = [
#  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 
#  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#  "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#  "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
#]

# Puzzle input from https://adventofcode.com/2023/day/1/input
file = open("02_input.txt", "r")
gamesLines = file.readlines()

class Game (object):
  def __init__(self, gameID):
    self.gameID = gameID
    self.red = 0
    self.green = 0
    self.blue = 0
    
  @property
  def power(self):
    return self.red * self.green * self.blue
    
  def __str__(self):
    return f"Game {self.gameID}: Max count {self.red} red, {self.green} green, {self.blue} blue"

class Games (object):
  def __init__(self, gamesLines):
    self.gameslist = []
    self.parseGames(gamesLines)

  def parseGames(self, gamesLines):
    for gameText in gamesLines:
      gameIDText, gameRollsText = gameText.split(":")
      gameID = int(re.findall("\d+", gameIDText)[0])
      game = Game(gameID)
      # print(game)
    
      gameRolls = gameRollsText.split(";")
      if len(gameRolls) > 0:
        for roll in gameRolls:
            dice = roll.split(",")
            for die in dice:
              # find the number of dice and then put it in the right color
              dieCount = int(re.findall("\d+", die)[0])
              if "red" in die and dieCount > game.red:
                game.red = dieCount
              if "green" in die and dieCount > game.green:
                game.green = dieCount
              if "blue" in die and dieCount > game.blue:
                game.blue = dieCount
        self.gameslist.append(game)
        #print(game)
          
  def printResult(self):
    result = 0
    for game in self.gameslist:
      result += game.power
    print(f"Here's the result: {result}")
          
  
  
if __name__ == '__main__':
  # do the parsing and comparing
  games = Games(gamesLines)
  games.printResult()
