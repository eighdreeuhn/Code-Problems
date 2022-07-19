# This seems like a lot af fun!


def maze_runner(maze, directions):
    position = []
    for row in range(0, len(maze)):
        for column in range(0, len(maze[0])):
            if maze[row][column] == 2:
                position = [row, column]
    for move in directions:
        if move == 'N':
            position[0] -= 1
        elif move == 'S':
            position[0] += 1
        elif move == 'E':
            position[1] += 1
        elif move == 'W':
            position[1] -= 1
        if maze[position[0]][position[1]] == 1 or position[0] < 0 or position[1] < 0 or position[0] >= len(maze) or position[1] >= len(maze):
            return 'Dead'
        elif maze[position[0]][position[1]] == 3:
            return 'Finish'
    return 'Lost'


maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1]]

directions = ["N","N","N","N","N","E","E","E","E","E"]

print(maze_runner(maze, directions))