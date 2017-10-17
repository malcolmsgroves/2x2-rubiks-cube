# Dijkstra
An implementation of the Dijkstra graph search algorithm that finds the shortest path from two locations in the United States. 

## Install and Run
Download the repository from GitHub. Open Terminal and ```cd``` into the local directory. 
To search for the shortest path between Boston and Berkley, type 

> python dijkstra.py < tests/0boston_berkeley.in

To generate a kml file containing the shortest path between Boston and Berkely, type 

> TRACE=kml python dijkstra.py < tests/0boston_berkeley.in

A .kml file will be generated in the local directory. These .kml files can be visualized in [Google My Maps](https://www.google.com/maps/d/u/0/). A sample map can be viewed [here](https://drive.google.com/open?id=1ibJ7-uEdVi08QoRTPhq4o01nExs&usp=sharing). Other possible routes to search can be found in the ```tests/``` directory.
To test the program, type 

> python dijkstra_test.py

This tests the algorithm on four preset routes.

## Implementation
The priority queue for the Dijkstra search algorithm is implemented with a min-heap that maps keys to heap indices. Extracting the minimum key takes O(1) time and decreasing a key takes O(log*n*) time.
The algorithm consists of 4 steps:
1.  Remove the min-key from the priority queue and make its distance permanent.
2.  Check if the min-key is the destination node. If it is, shortest path is found - exit loop.
3.  Relax all the edges from the min-key to adjacent nodes and add adjacent nodes to priority queue.

The runtime for this program is O(|E| + |V| * log|V|) where E is the set of all edges and V is the set of all nodes (vertices).

```python
   def dijkstra(self, weight, nodes, source, destination):
        """Performs Dijkstra's algorithm until it finds the shortest
        path from source to destination in the graph with nodes and edges.
        Assumes that all weights are non-negative.
    
        Args:
            weight: function for calculating the weight of edge (u, v). 
            nodes: list of all nodes in the network.
            source: the source node in the network.
            destination: the destination node in the network.
         
        Returns:
            A tuple: (the path as a list of nodes from source to destination, 
                      the number of visited nodes)
        """
        
        num_visited = 0
        
        # instantiate set of node vertices
        for node in nodes:
            node.parent = None
            node.queue_key = None
        
        # instantiate source node with distance 0
        source.queue_key = NodeDistancePair(source, 0)
        source.parent = None
        
        # instantiate min-heap priority queue with source node
        heapq = PriorityQueue()
        heapq.insert(source.queue_key)
        
        # while nodes are contained in the min-heap
        while len(heapq) > 0:
            
            # extract the node with the minimum key
            node_key = heapq.extract_min()
            node, dist = node_key.node, node_key.distance
            num_visited += 1
            
            # if we have discovered the shortest path to the destination
            if node is destination: break
            
            # relax all adjacent nodes 
            for v in node.adj:
                v_dist = weight(node, v) + dist
                if v.queue_key is None:
                    v.parent = node
                    v.queue_key = NodeDistancePair(v, v_dist)
                    heapq.insert(v.queue_key)
                elif v.queue_key.distance > v_dist:
                    v.parent = node
                    v.queue_key.distance = v_dist;
                    heapq.decrease_key(v.queue_key)
        
        path = []       
        
        # follow shortest path back from destination
        while destination is not None:
            path.insert(0, destination)
            destination = destination.parent           
                    
        return (path, num_visited)
```
