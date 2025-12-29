"""
You need to get to the cafeteria that's on the other side of the back wall.

There are big rolls of paper lying around that forklifts are busy
moving.
If you can optimize the work the forklifts are doing, then they will 
have spare time to break through the wall.

The rolls of paper (@) are arranged on a large grid.
The forklifts can only access a roll of paper if there are fewer than 4
rolls of paper in the eight adjacent positions.
(.) are empty spaces on the grid

Your goal is to figure out how many rolls of paper the forklifs can access
"""

def printGrid(grid):
    for row in grid:
        print(row)

def getRolls(grid: list[list[str]]) -> int:
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):

            # Check if space is a roll
            if (grid[y][x] == "@"):
                # Count rolls in adjacent squares
                rolls = countAdjacentRolls(grid, x, y)
                if (rolls < 4):
                    res += 1
    
    return res

def countAdjacentRolls(grid: list[list[str]], x: int, y: int) -> int:
    x_before, x_after = x-1, x+1
    y_before, y_after = y-1, y+1

    tl = grid[y_before][x_before] if (y_before >= 0 and x_before >= 0) else "."
    tm = grid[y_before][x] if (y_before >= 0) else "."
    tr = grid[y_before][x_after] if (y_before >= 0 and x_after < len(grid[y])) else "."

    lm = grid[y][x_before] if (x_before >= 0) else "."
    rm = grid[y][x_after] if (x_after < len(grid[y])) else "."

    bl = grid[y_after][x_before] if (y_after < len(grid) and x_before >= 0) else "."
    bm = grid[y_after][x] if (y_after < len(grid)) else "."
    br = grid[y_after][x_after] if (y_after < len(grid) and x_after < len(grid[y])) else "."

    sub_grid = [tl, tm, tr, lm, rm, bl, bm, br]
    return sum(1 for x in sub_grid if x == "@")




def test():
    correct = 13
    grid = []
    with open("test", "r") as f:
        while True:
            line = f.readline().strip()

            if (not line):
                break

            row = [x for x in line]
            grid.append(row)

        rolls = getRolls(grid)

        assert correct == rolls
        print(f"Accessible Rolls: {rolls}")

        
def main():
    grid = []
    with open("input", "r") as f:
        while True:
            line = f.readline().strip()

            if (not line):
                break

            row = [x for x in line]
            grid.append(row)

        rolls = getRolls(grid)
        print(f"Accessible Rolls: {rolls}")
        
# test()
main()