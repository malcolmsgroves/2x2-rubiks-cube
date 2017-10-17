# Rubik
Solves a 2 x 2 rubik's cube using a two-way breadth-first search that runs in O(5<sup>n/2</sup>) time, where 5 is the number of new twists possible and n is the number of moves required to solve the cube.

## Install and Run Tests
Download the project from GitHub. Open terminal and ```cd``` into the local repository. To run tests, type
> python test_solver.py

This command will run the tests in the test_solver.py file, solves four rubik's cube configurations using the *shortest_path* method in solver.py. The methods for manipulating the rubik's cube object are included in the rubik.py file.

## Implementation
This program implements a two-way breadth-first search by storing the rubik's cube positions as dictionary keys and the parent nodes and node levels as dictionary values. On each iteration, the algorithm completes four steps:
1.  For all nodes in the start node frontier, get adjacent nodes using the six possible quarter twists. If the adjacent node is not already visited, add the node and the move to the dictionaries.
2.  For all nodes in the end node frontier, get adjacent nodes using the six possible quarter twists. If the adjacent node is not already visited, add the node and the inverse move to the dictionaries.
3.  If a node in the end node frontier is in the start node dictionary, shortest path is found - exit loop.
4.  Return to step 1.

*shortest_path* method in the solver.py file
```python
def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    """
    
    # keep track of vertex levels and parents
    front_level = {start: 0}
    back_level = {end: 0}
    front_parent = {start: (None, None)}
    back_parent = {end: (None, None)}
    
    i = 1       # i = level
    
    convergence = None
    front_frontier = [start]
    back_frontier = [end]
    
    # conduct two-source BFS from start and end
    while convergence is None:
        front_next = []
        back_next = []
        
        # expand start frontier with new moves
        for u in front_frontier:
            for move in rubik.quarter_twists:
                v = rubik.perm_apply(move, u)   
                if v not in front_level:
                    front_level[v] = i              # level
                    front_parent[v] = (u, move)     # parent  
                    front_next.append(v)            # add to new frontier
        
        # overwrite frontier with new vertices
        front_frontier = front_next
        
        # expand end frontier with new moves
        for u in back_frontier:
            for move in rubik.quarter_twists:
                v = rubik.perm_apply(move, u)
                if v not in back_level:
                    back_level[v] = i                               # level
                    back_parent[v] = (u, rubik.perm_inverse(move))  # parent      
                    back_next.append(v)                             # add to frontier
                    
                    #check if v has been discovered by the start BFS
                    if v in front_level:
                        convergence = v
                        continue
        
        # overwrite frontier with new vertices
        back_frontier = back_next
        
        i += 1
    
    solution = []
    front_curr = convergence
    back_curr = convergence
    
    # add shortest path from start -> convergence to solution
    while front_parent[front_curr][0] is not None:
        solution.insert(0, front_parent[front_curr][1])
        front_curr = front_parent[front_curr][0]
        
    # add shortest path from convergence -> end to solution  
    while back_parent[back_curr][0] is not None:
        solution.append(back_parent[back_curr][1])
        back_curr = back_parent[back_curr][0]
        
    
        
    return solution
```
