# MIT Algorithms
This directory contains exercises from the MIT 6.006 Fall 2011 *Introduction to Algorithms*. Course materials can be found [at their website](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/index.htm). In general, the code provided included: file I/O, data classes, and tests. I wrote the algorithms to solve the problems described below. See README.md files in individual project directories for more information.

## 2 x 2 Rubik's Cube
Solves a 2 x 2 rubik's cube using a two-source breadth-first search (BFS) that starts at the start and end configurations. If n moves are required to solve the rubik's cube, the two-source BFS implementation runs in O(5<sup>n/2</sup>) time while the single source implementation would run in O(5<sup>n</sup>) time.
