def maze_runner(maze, directions):
    x = None 
    y = None
    
    for i, row in enumerate(maze):
        for j, column in enumerate(maze):
            if maze[i][j] == 2:
                x = i
                y = j
                break
                
    for dir in directions:
        if dir == "N":
            x -= 1
        elif dir == "S":
            x += 1
        elif dir == "W":
            y -= 1
        else:
            y += 1
        if x >= len(maze) or y >= len(maze[0]) or x < 0 or y < 0 or maze[x][y] == 1:
            return "Dead"
        if maze[x][y] == 3:
            return "Finish"
    
    return 'Lost'
    
    