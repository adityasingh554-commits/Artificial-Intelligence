MOVES = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

def solve_dfs(state, goal, visited, depth):
    if state == goal:
        return []

  
    if depth > 10: 
        return None

    
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)

   
    for dr, dc, move_name in MOVES:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr * 3 + nc
            
            
            next_state = list(state)
            next_state[zero_idx], next_state[new_idx] = next_state[new_idx], next_state[zero_idx]
            next_state = tuple(next_state)

            
            if next_state not in visited:
                visited.add(next_state)
                
                
                result = solve_dfs(next_state, goal, visited, depth + 1)
                
                
                if result is not None:
                    return [move_name] + result
                    
                visited.remove(next_state)

    return None


start = (1, 2, 3, 
         4, 0, 5, 
         7, 8, 6)

goal  = (1, 2, 3, 
         4, 5, 6, 
         7, 8, 0)


path = solve_dfs(start, goal, visited={start}, depth=0)

print("Moves to solve:", path)