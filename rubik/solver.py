import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
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

def testShortestPath4():
        """Length 4 path."""
        start = rubik.I
        middle1 = rubik.perm_apply(rubik.F, start)
        middle2 = rubik.perm_apply(rubik.L, middle1)
        middle3 = rubik.perm_apply(rubik.F, middle2)
        end = rubik.perm_apply(rubik.L, middle3)
        print(rubik.perm_to_string(rubik.F))
        print(rubik.perm_to_string(rubik.L))
        print(rubik.perm_to_string(rubik.F))
        print(rubik.perm_to_string(rubik.L))
        ans = shortest_path(start, end)
        print(assertGoodPath(start, end, ans))
        return ans

def assertGoodPath(start, end, path):
        current = start
        for move in path:
            current = rubik.perm_apply(move, current)
        return current == end
        
        
if __name__ == '__main__':
    ans = (testShortestPath4())
    for move in ans:
        print(rubik.perm_to_string(move))
    
    
         
                    
                    
    
    # raise NotImplementedError
