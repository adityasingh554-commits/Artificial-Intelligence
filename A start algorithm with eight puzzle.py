import heapq


GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8), 6: (3, 7), 7: (4, 6, 8), 8: (5, 7)}

def solve_8_puzzle(start):
    queue = [(0, 0, start, [start])]
    visited = {start}

    while queue:
        _, g, board, path = heapq.heappop(queue)

        if board == GOAL:
            return path

        blank = board.index(0)
        for move in MOVES[blank]:
            next_board = list(board)
            next_board[blank], next_board[move] = next_board[move], next_board[blank]
            next_board = tuple(next_board)

            if next_board not in visited:
                visited.add(next_board)
                
                
                h = sum(abs(i//3 - GOAL.index(v)//3) + abs(i%3 - GOAL.index(v)%3) 
                        for i, v in enumerate(next_board) if v != 0)
                
                heapq.heappush(queue, (g + 1 + h, g + 1, next_board, path + [next_board]))
    return None


start_board = (1, 3, 0, 4, 2, 5, 7, 8, 6)
solution = solve_8_puzzle(start_board)

if solution:
    print(f"Solved in {len(solution) - 1} steps!")
    for step, board in enumerate(solution):
        print(f"Step {step}: {board[0:3]} {board[3:6]} {board[6:9]}")
else:
    print("Unsolvable board configuration.")
