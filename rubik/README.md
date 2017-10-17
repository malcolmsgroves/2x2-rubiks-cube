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

```python

```
