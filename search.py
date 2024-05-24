# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    S = util.Stack()
    S.push((problem.getStartState(), []))
    visited_nodes = set()

    while not S.isEmpty():

        current_node, moves = S.pop()

        if problem.isGoalState(current_node):
            return moves
        
        visited_nodes.add(current_node)
        nodes = problem.getSuccessors(current_node)

        for next_node, action, _ in nodes:
            if next_node not in visited_nodes:
                S.push((next_node, moves + [action]))

    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    Q = util.Queue()
    visited_nodes = set()
    Q.push((problem.getStartState(), [], 0))
    while not Q.isEmpty():
        current_nodes, moves, Cost = Q.pop()

        if current_nodes not in visited_nodes:
            visited_nodes.add(current_nodes)
            if problem.isGoalState(current_nodes):
                return moves
            else:
                nodes = problem.getSuccessors(current_nodes)
                for next_nodes, action, nextCost in nodes:
                    newAction = moves + [action]
                    newCost = Cost + nextCost
                    child = (next_nodes, newAction, newCost)
                    Q.push(child)

    return moves

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    Q = util.PriorityQueue()
    Q.push((problem.getStartState(), []),0)
    visited_nodes = set()
    while not Q.isEmpty():
        current_node, moves = Q.pop()
        if problem.isGoalState(current_node):
            return moves
        if current_node not in visited_nodes:
            next_nodes = problem.getSuccessors(current_node)
            for next in next_nodes:
                peculiarities = next[0]
                if peculiarities not in visited_nodes:
                    directions = next[1]
                    newCost = moves + [directions]
                    Q.push((peculiarities, moves + [directions]), problem.getCostOfActions(newCost))
        visited_nodes.add(current_node)
    return []
    util.raiseNotDefined()
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited_nodes = set()
    Q = util.PriorityQueue()
    Q.push((problem.getStartState(), []),nullHeuristic((problem.getStartState(),[]), problem))
    n_cost = 0
    while not Q.isEmpty():
        current_node, moves = Q.pop()
        if problem.isGoalState(current_node):
            return moves
        if current_node not in visited_nodes:
            next_nodes = problem.getSuccessors(current_node)
            for next in next_nodes:
                peculiarities = next[0]
                if peculiarities not in visited_nodes:
                    directions = next[1]
                    n_actions = moves + [directions]
                    n_cost = problem.getCostOfActions(n_actions) + heuristic(peculiarities, problem)
                    Q.push((peculiarities, moves + [directions]), n_cost)
        visited_nodes.add(current_node)
    return moves
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
