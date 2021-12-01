coordinates = (
            (0,1), 
            (0,2), 
            (0,3), 
            (0,4), 
            (1,1), 
            (2,1), 
            (2,3), 
            (3,3), 
            (4,0), 
            (4,1), 
            (4,2), 
            (4,3),
            )
start = [0,0]
finish = [4,4]
position = start

def createMaze(coordinates, start, finish):
    maze = []
    for x in range(5):
        row = []
        for y in range(5):
            if tuple([x, y]) in coordinates:
                row.append("X")
            elif list([x, y]) == start:
                row.append("S")
            elif list([x, y]) == finish:
                row.append("F")
            else:
                row.append(" ")
        maze.append(row)
    return maze

def validPosition(x, y):
    if (x < 0) | (y < 0):
        return False
    if (x > 4) | (y > 4):
        return False
    if maze[x][y] == " ":
        return True
    if maze[x][y] == "F":
        return True
    return False

def solveMaze(maze, position):
    movements = []
    while len(movements) >= 0:
        if validPosition(position[0] + 1, position[1]):
            maze[position[0]][position[1]] = "-"
            position = [position[0] + 1, position[1]]
            movements.append("Down")
        if validPosition(position[0] - 1, position[1]):
            maze[position[0]][position[1]] = "-"
            position = [position[0] - 1, position[1]]
            movements.append("Up")
        if validPosition(position[0],position[1] + 1):
            maze[position[0]][position[1]] = "-"
            position = [position[0], position[1] + 1]
            movements.append("Right")
        if validPosition(position[0], position[1] - 1):
            maze[position[0]][position[1]] = "-"
            position = [position[0], position[1] - 1]
            movements.append("Left")
        if maze[position[0]][position[1]] == "F":
            break
    return movements

maze = createMaze(coordinates, start, finish) 

print(maze[0])
print(maze[1])
print(maze[2])
print(maze[3])
print(maze[4])

movements = solveMaze(maze, position)

print("\nThe solution of the maze has been marked with '-':\n")
print(maze[0])
print(maze[1])
print(maze[2])
print(maze[3])
print(maze[4])

print("\nThe maze has been finished with this list of movements:\n" + str(movements))