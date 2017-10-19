# MIT Algorithms
This directory contains exercises from the MIT 6.006 Fall 2011 *Introduction to Algorithms*. Course materials can be found [at their website](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/index.htm). In general, the code provided included: file I/O, data classes, and tests. I wrote the algorithms to solve the problems described below. See README.md files in individual project directories for more information.

## 2 x 2 Rubik's Cube
Solves a 2 x 2 rubik's cube using a two-source breadth-first search (BFS) that starts at the start and end configurations. If n moves are required to solve the rubik's cube, the two-source BFS implementation runs in O(5<sup>n/2</sup>) time while the single source implementation would run in O(5<sup>n</sup>) time.

## Shortest Path
Discovers the shortest path on roads between two locations in the United States using Dijkstra's algorithm for directed acyclic graphs (DAGs). Given a set of nodes V and a set of edges E, the runtime for this program is O(|E| + |V| * log|V|). The priority queue is implemented with a min-heap that maps keys to indices so that the *decrease_key* operation is O(log*n*) and the *extract_min* operation is O(1).

## Resize Image
Resizes an image without distortion by removing seams in the image. The seam with the least *energy* is removed. *Energy* quantifies the sum of the difference in magnitude for each pixel in the seam from its neighboring pixels. Seams are identified in O(w x h) time using dynamic programming. A vertical seam in shown in red in the image below.

![Sunset Seam](https://github.com/malcolmsgroves/mit-algorithms/blob/master/resize-image/seam.png)

## Text Justification
Prints a .txt file to the console with optimized justification. The "badness" of each line is equal to (PAGE_WIDTH - *line_length*)<sup>3</sup> if *line_length* <= PAGE_WIDTH and infinity otherwise. The total "badness" is optimized using a dynamic programming strategy that runs in O(n<sup>2</sup>) time.
