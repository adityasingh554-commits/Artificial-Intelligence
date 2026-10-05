MOVES = [(-1,0,'Up'), (1,0,'Down'), (0,-1,'Left'), (0,1,'Right')]

def dls(state, goal, limit, path):
    if state == goal:
        return path
    if len(path) >= limit:
        return None

    idx = state.index(0)
    r, c = idx // 3, idx % 3

    for dr, dc, name in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            
            nxt = list(state)
            nxt[idx], nxt[nr*3 + nc] = nxt[nr*3 + nc], nxt[idx]
            nxt = tuple(nxt)

            
            if not path or name != path[-1]: 
                result = dls(nxt, goal, limit, path + [name])
                if result: 
                    return result
    return None

def iddfs(start, goal):
    
    limit = 0
    while True:
        result = dls(start, goal, limit, [])
        if result is not None:
            return result
        limit += 1


start = (1, 2, 3, 
         4, 0, 5, 
         7, 8, 6)

goal  = (1, 2, 3, 
         4, 5, 6, 
         7, 8, 0)

print("Shortest path:", iddfs(start, goal))
