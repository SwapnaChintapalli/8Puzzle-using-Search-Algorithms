import puzzle
import sys
import math

puzzleString=3
puzzleArray=puzzleString.split(" ")
p=puzzle.TilePuzzle(int(math.sqrt(len(puzzleArray))))
p.readPuzzle(puzzleString)
p.parseMoveSequence(10)
print(p.checkPuzzle())



