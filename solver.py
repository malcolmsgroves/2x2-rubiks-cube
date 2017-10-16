import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    front_level = {start: 0}
    back_level = {end: 0}
    front_parent = {start: (None, None)}
    back_parent = {end: (None, None)}
    
    i = 1
    convergence = None
    front_frontier = [start]
    back_frontier = [end]
    
    while convergence is None:
        front_next = []
        back_next = []
        for u in front_frontier:
            for move in rubik.quarter_twists:
                v = rubik.perm_apply(move, u)   # this might be backwards
                if v not in front_level:
                    front_level[v] = i
                    front_parent[v] = (u, move)     # changed from u to track moves
                    front_next.append(v)
        front_frontier = front_next
        for u in back_frontier:
            for move in rubik.quarter_twists:
                v = rubik.perm_apply(move, u)
                if v not in back_level:
                    back_level[v] = i
                    back_parent[v] = (u, rubik.perm_inverse(move))       # changed from u to track moves
                    back_next.append(v)
                    if v in front_level:
                        convergence = v
                        continue
        back_frontier = back_next
        i += 1
    
    solution = []
    front_curr = convergence
    back_curr = convergence
    
    while front_parent[front_curr][0] is not None:
        solution.insert(0, front_parent[front_curr][1])
        front_curr = front_parent[front_curr][0]
        
        
    
        
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
