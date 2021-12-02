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
    if maze[x][y] == "X":
        return False
    return True

def printMaze(maze):
    print(maze[0])
    print(maze[1])
    print(maze[2])
    print(maze[3])
    print(maze[4])    

def playerPosition(maze, position):
    if validPosition(position[0], position[1]):
        if maze[position[0]][position[1]] != "F":
            maze[position[0]][position[1]] = "@"

def oldPosition(maze, position):
    if maze[position[0]][position[1]] != "S":
        maze[position[0]][position[1]] = " "
     
def solveMaze(maze, position):
    movements = []
    while len(movements) >= 0:
        printMaze(maze)
        movement = input("Which way do you want to go?: ")
        movement = movement.capitalize() 

        if movement == "Down":
            if validPosition(position[0] + 1, position[1]) == False:
                print("There is a wall here! You can't go this way!")
            else:
                movements.append("Down")
                oldPosition(maze, position)
                position = [position[0] + 1, position[1]]
                playerPosition(maze, position)

        if movement == "Up":
            if validPosition(position[0] - 1, position[1]) == False:
                print("There is a wall here! You can't go this way!")
            else:
                movements.append("Up")
                oldPosition(maze, position)
                position = [position[0] - 1, position[1]]
                playerPosition(maze, position)
                
        if movement == "Right":
            if validPosition(position[0], position[1] + 1) == False:
                print("There is a wall here! You can't go this way!")
            else:
                movements.append("Right")
                oldPosition(maze, position)
                position = [position[0], position[1] + 1]
                playerPosition(maze, position)

        if movement == "Left":
            if validPosition(position[0], position[1] - 1) == False:
                print("There is a wall here! You can't go this way!")
            else: 
                movements.append("Left")
                oldPosition(maze, position)
                position = [position[0], position[1] - 1]            
                playerPosition(maze, position)

        if maze[position[0]][position[1]] == "F":
            break

    print("\nCongratulations! You've passed the game.")
    return movements

maze = createMaze(coordinates, start, finish)

print("\nWelcome to The Maze! You have to reach the exit (marked with 'F') by moving your character (represented with '@').\nYou have the folowing movements available: Down, Up, Left or Right.\nYour starting point is the box 'S'. Good luck with solving the maze!\n")

movements = solveMaze(maze, position)

print("\nThe maze has been finished with this list of movements:\n" + str(movements))