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

maze = createMaze(coordinates, start, finish) 
position = start

def validPosition(position):
    for i in position:
        if any(i < 0):
            return False
        if any(i == "X"):
            return False
        if any(i == " "):
            return True

print(maze[0])
print(maze[1])
print(maze[2])
print(maze[3])
print(maze[4])

def solveMaze(maze, position):
    movements = []
    while len(movements) >= 0:
        if validPosition(position[0] + 1):
            position = [position[0] + 1, position[1]]
            movements.append("Down")
        if validPosition(position[0] - 1):
            position = [position[0] - 1, position[1]]
            movements.append("Up")
        if validPosition(position[1] + 1):
            position = [position[0], position[1] + 1]
            movements.append("Right")
        if validPosition(position[1] - 1):
            position = [position[0], position[1] - 1]
            movements.append("Left")
        if validPosition(position) == "F":
            break
    return movements

movements = solveMaze(maze, position)

print("The maze has been finished with this list of movements:\n" + str(movements))