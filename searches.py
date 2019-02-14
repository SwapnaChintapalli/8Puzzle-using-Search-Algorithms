'''
Code written by Ricardo Soares
------------------------------
University of Aberdeen
MSc Artificial Intelligence
Written in Python 2.7.14
'''

import puzzle
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
import node
import sys
from test.test_largefile import size
class Search:

    '''
    Instantiates the class, defining the start node
    '''
    def __init__(self, puzzle):
        self.start = node.Node(puzzle)

    '''
    Best First Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''

    def bestFirst(self):
        closed = list()
        leaves = Queue()
        leaves.put(self.start)
        qcount = 0
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            print(actual)
            totalMoves = str(actual)
            if totalMoves.__len__() > 10:
                print("goal state was not found before or at depth 10")
                return
            if actual.goalState():
                print("Number of moves: ",totalMoves.__len__())
                print("Number of states enqueued: ",qcount-1)
                return actual
            elif actual.state.puzzle not in closed:
                
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())
            qcount=qcount+1
#         return leaves
    '''
    Iterative Deepening Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''
    def iterativeDeepening(self):
        depth = 0
        result = None
        while result == None:
            ids_count = 0
            result = self.depthLimited(depth,ids_count)
            depth +=1
            if depth > 10:
                print("goal state was not found before or at depth 10")
                return
            if result != None :
                print("ENqueued count:",ids_count)
        return result
    
    '''
    Depth Limited Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''

    def depthLimited(self, depth,ids_count):
#         qcount = 1
        leaves = LifoQueue()
        leaves.put(self.start)
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
#             ids_count = ids_count + 1
            print(actual)
            if actual.goalState():
                print("Total no.of moves ",actual.depth)
                print("Number of states enqueued: ",ids_count-1)
                return actual
            elif actual.depth is not depth:
                
                succ = actual.succ()
                while not succ.empty():
#                     ids_count = ids_count + 1
                    leaves.put(succ.get())
            ids_count = ids_count + 1
    '''
    Greedy Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''

    def greedy(self, heuristic):
        qcount = 1
        actual = self.start
        leaves = PriorityQueue()
        leaves.put((actual.costHeur(heuristic), actual))
        closed = list()
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()[1]
            print(actual)
            if actual.goalState():
                print("Number of Moves: ",qcount)
                return actual
            elif actual.state.puzzle not in closed:
                qcount = qcount + 1
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    child = succ.get()
                    leaves.put((child.costHeur(heuristic), child))
            
    ''' 
    A* Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
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
            
            print(actual)
            totalMoves =str(actual)
            if totalMoves.__len__() > 10:
                print("goal state was not found before or at depth 10")
                return
            if actual.goalState():
                print("Number of Moves: ",totalMoves.__len__())
                print("Number of states Enqueued", qcount-1)
                return actual
            elif actual.state.puzzle not in closed:
                
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    child = succ.get()
                    leaves.put((child.costHeur(heuristic)+child.depth, child))
#                     qcount = qcount + 1
            qcount = qcount + 1