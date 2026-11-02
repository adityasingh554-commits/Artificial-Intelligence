def hill_climb(start):
    current = start

    while True:
        neighbours = [current-1, current + 1]
        best_neighbours = max(neighbours)


        if best_neighbours > current:
            current = best_neighbours
        else:
            break
        heurisitc = 0
        print("Heuristic",heurisitc)
        return current


print(hill_climb(3))