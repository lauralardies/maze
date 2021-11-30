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
start = (0, 0)
finish = (4, 4)

def createMaze(coordinates, start, finish):
    maze = []
    for x in range(5):
        row = []
        for y in range(5):
            if tuple([x, y]) in coordinates:
                row.append("X")
            elif tuple([x, y]) == start:
                row.append("S")
            elif tuple([x, y]) == finish:
                row.append("F")
            else:
                row.append(" ")
        maze.append(row)
    return maze

maze = createMaze(coordinates, start, finish) 
position = start
movements = []

print(maze[0])
print(maze[1])
print(maze[2])
print(maze[3])
print(maze[4])

while True: 
    while position in range(5):
        if " " ==  position[0] + 1:
            movements.append("Down")
            position = [position[0] + 1, position[1]]
        elif " " == position[0] - 1: 
            movements.append("Up")
            position = [position[0] - 1, position[1]]
        elif " " == position[1] + 1: 
            movements.append("Right")
            position = [position[0], position[1] + 1]
        elif " " == position[1] - 1: 
            movements.append("Left")
            position = [position[0], position[1] - 1]
        elif position == finish:

            break
    break

print("The maze has been finished with this list of movements: \n" + str(movements))