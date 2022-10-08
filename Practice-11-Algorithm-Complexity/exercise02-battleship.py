def battleship(grid, line, column):
    if (grid[line][column] == 1):
        return True
    return False


grid = [[0, 0, 0, 0, 1], [0, 1, 0, 1, 0]]

print(battleship(grid, 1, 3))

# Ordem de complexidade = O(1)
