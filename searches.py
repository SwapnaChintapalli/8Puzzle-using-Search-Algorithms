from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
import node
class Search:

    '''
    Instantiates the class, defining the start node
    '''
    def __init__(self, puzzle):
        self.start = node.Node(puzzle)

    '''
    Breadth First Search Algorithm 
    '''

    def breadthFirst(self):
        closed = list()
        leaves = Queue()
        leaves.put(self.start)
        qcount = -1
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            print(actual)
            totalMoves = str(actual)
            if totalMoves.__len__() > 10:
                print("Failure: Goal state was not found before or at depth 10")
                return
            if actual.goalState():
                print("Number of Moves: ",totalMoves.__len__())
                print("Number of States Enqueued: ",qcount)
                return actual
            elif actual.state.puzzle not in closed:
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())
            qcount=qcount+1
#         return leaves
    '''
    Iterative Deepening Search Algorithm
    '''
    def iterativeDeepening(self):
        depth = 0
        result = None
        while result == None:
            ids_count = 0
            result = self.depthLimited(depth,ids_count)
            depth +=1
            if depth > 10:
                print("Failure: Goal state was not found before or at depth 10")
                return
        return result
    
    '''
    Depth Limited Search Algorithm
    '''

    def depthLimited(self, depth,ids_count):
        leaves = LifoQueue()
        leaves.put(self.start)
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            print(actual)
            if actual.goalState():
                print("Total no.of Moves: ",actual.depth)
                print("Number of States Enqueued: ",ids_count-1)
                return actual
            elif actual.depth is not depth:
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())
            ids_count = ids_count + 1
            
    ''' 
    A* Search Algorithm "
    '''

    def aSearch(self, heuristic):
        heur = heuristic
        qcount = 0
        actual = self.start
        leaves = PriorityQueue()
        leaves.put((actual.costHeur(heuristic), actual))
        closed = list()
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()[1]
#             print(actual)
            totalMoves =str(actual)
            if totalMoves.__len__() > 10:
                print("Failure: Goal state was not found before or at depth 10")
                return
            if actual.goalState():
                print("Number of Moves: ",totalMoves.__len__())
                print("Number of states Enqueued: ", qcount-1)
                return actual
            elif actual.state.puzzle not in closed:
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    child = succ.get()
                    leaves.put((child.costHeur(heuristic)+child.depth, child))
            qcount = qcount + 1