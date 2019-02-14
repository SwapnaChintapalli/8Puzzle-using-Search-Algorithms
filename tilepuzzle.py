import puzzle 
import sys
import searches

t=puzzle.TilePuzzle(3)
# t.permute(int(10))
puz = input()
t.readPuzzle(puz)
t.printPuzzle()
s=searches.Search(t)
print("Enter Search Algo:")
srch = str(input())
print(srch)
if srch == 'bfs':
    print("Considering Best First:", s.bestFirst())
elif srch == "ids":
    print("Considering Iterative Deepening Search:", s.iterativeDeepening())
elif srch == 'astar1':
    print("Considering A* 1 Search:", s.aSearch(0))
elif srch == 'astar2':
    print("Considering A* 2 Search:", s.aSearch(1))