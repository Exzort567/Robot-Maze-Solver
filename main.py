maze = [[".", ".", ".", "."],
        [".", "x", "x", "x"],
        [".", ".", ".", "."],
        ["x", "x", "x", "."]]


def print_maze(maze):
    for row in maze:
        row_maze = ""
        for value in row:
            row_maze += value + " "
        print(row_maze)


def solve_maze(maze):
    if len(maze) < 1:
        return None
    if len(maze[0]) < 1:
        return None
    return solve_maze_sol(maze, [], 0, 0)


def solve_maze_sol(maze, sol, pos_col, pos_row):
    num_row = len(maze)
    num_col = len(maze[0])
    #base case

    if pos_row == num_row - 1 and pos_col == num_row - 1:
        return sol
    
    if pos_row >= num_row or pos_col >= num_col:
        return None

    if maze[pos_row][pos_col] == "x": 
        return None

    #recusive case
    sol.append("r")
    sol_going_right = solve_maze_sol(maze, sol, pos_col + 1, pos_row)
    if sol_going_right is not None:
        return sol_going_right
    
    sol.pop()
    sol.append("d")
    sol_going_down = solve_maze_sol(maze, sol, pos_col, pos_row + 1)
    if sol_going_down is not None:
        return sol_going_down

    sol.pop()
    return None


print_maze(maze) 
solution = solve_maze(maze)
if solution:
    print("Solution", solution)
else:
    print("No solution")    