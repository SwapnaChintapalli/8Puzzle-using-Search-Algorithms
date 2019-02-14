import puzzle 
import searches
import time
t=puzzle.TilePuzzle(3)
print("Enter initial state:")
puz = input()
t.readPuzzle(puz)
t.printPuzzle()
s=searches.Search(t)
print("Enter Search Algo:")
srch = str(input())
if srch == 'bfs':
    print("Breadth First Search:")
    start = time.time()
    string = s.breadthFirst()
    end = time.time()
elif srch == "ids":
    print("Iterative Deepening Search:")
    start = time.time()
    string = s.iterativeDeepening()
    end = time.time()
elif srch == 'astar1':
    print("A* 1 Search:")
    start = time.time()
    string = s.aSearch(0)
    end = time.time()
elif srch == 'astar2':
    print("A* 2 Search:")
    start = time.time()
    string = s.aSearch(1)
    end = time.time()
else:
    print("Invalid Search Algorithm")
    
if string!= None:
    print("Total Time: ",end-start," seconds")
    t.parseMoveSequence(string)