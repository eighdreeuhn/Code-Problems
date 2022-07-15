def get_generation(cells, generation):

    def count_neighbors(r, c, matrix):
        width = len(matrix[0])
        height = len(matrix)
        n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # print((r, c), (r + i) % height, (c + j) % width, matrix[(r + i) % height][(c + j) % width])
                if matrix[(r + i) % height][(c + j) % width] == 1 and not (i == 0 and j == 0):
                    n += 1
        return n

    for gen in range(0, generation):
        cells_copy = cells.copy()
        for k, row in enumerate(cells):
            for l, column in enumerate(row):
                # print(k, l, count_neighbors(k,  l, cells))
                if count_neighbors(k, l, cells) < 2 and cells[k][l] == 1:
                    cells_copy[k][l] = 0
                elif count_neighbors(k, l, cells) == 3 and cells[k][l] == 0:
                    cells_copy[k][l] = 1
                elif count_neighbors(k, l, cells) > 3 and cells[k][l] == 1:
                    cells_copy[k][l] = 0
        cells = cells_copy.copy()
        print(cells)
    return cells


cell_matrix = [[0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0],
               [0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0]]

get_generation(cell_matrix, 12)