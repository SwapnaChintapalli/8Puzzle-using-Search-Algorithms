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
# heur = 0
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
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            print(actual)
            if actual.goalState():
                print("TOtal no.of moves",closed.__len__())
                return actual
            elif actual.state.puzzle not in closed:
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())
#         return leaves
    '''
    Iterative Deepening Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''
    def iterativeDeepening(self):
        depth = 0
        result = None
        while result == None:
            result = self.depthLimited(depth)
            depth +=1
            if(depth >9):
                print("goal state was not found before or at depth 10")
                return
        return result
    
    '''
    Depth Limited Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''

    def depthLimited(self, depth):
        leaves = LifoQueue()
        leaves.put(self.start)
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            if actual.goalState():
                print("Total no.of moves ",actual.depth)
                return actual
            elif actual.depth is not depth:
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())

    '''
    Greedy Search Algorithm - Based in the pseudo code
    in "Artificial Intelligence: A Modern Approach - 3rd Edition"
    '''

    def greedy(self, heuristic):
        actual = self.start
        leaves = PriorityQueue()
        leaves.put((actual.costHeur(heuristic), actual))
        closed = list()
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()[1]
            if actual.goalState():
                return actual
            elif actual.state.puzzle not in closed:
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
        actual = self.start
        leaves = PriorityQueue()
        leaves.put((actual.costHeur(heuristic), actual))
        closed = list()
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()[1]
            if actual.goalState():
                return actual
            elif actual.state.puzzle not in closed:
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    child = succ.get()
                    leaves.put((child.costHeur(heuristic)+child.depth, child))