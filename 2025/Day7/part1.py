"""
You enter a teleporter hub and decide to step onto a large teleporter pad.
Suddently, you find yourself in an unfamilar room. The teleporter pad appears to be
leaking magic smoke.

After connecting some diagnostic tools, you find there is an issue with the tachyon manifolds.
You locate a diagram of the tachyon manifold (the input).

Tachyon beams pass start at (S).
They are free to pass through empty spaces (.)
If a beam encounters a splitter (^), the beam is stopped 
    and continues on from the immediate left and right

How many times will the beam split?
"""
def processBeam(grid, startX : int, startY: int):
    count = 0
    for row in range(startY, len(grid)):
        if (grid[row][startX] == "^"):
            count += 1

            grid[row][startX] = "X" # Mark the splitter as seen (X)

            if (startX - 1 >= 0):
                newGrid, res = processBeam(grid, startX-1, row)
                grid = newGrid
                count += res

            if (startX + 1 < len(grid)):
                newGrid, res = processBeam(grid, startX+1, row)
                grid = newGrid
                count += res

            break
        elif (grid[row][startX] == "."):
            grid[row][startX] = "|" # Mark the grid as traversed
        
        elif (grid[row][startX] == "X"):
            break   # If splitter has been visited, don't continue

    return grid, count

def findStart(grid):
    for col in range(len(grid[0])):
        if (grid[0][col] == "S"):
            return (col, 0)

def parseInput(infile: str):
    grid = []
    with open(infile, "r") as f:
        while (True):
            line = f.readline().strip()

            if (not line):
                break

            grid.append(list(line))
    return grid

def test():
    infile = "input"

    grid = parseInput(infile)
    startX, startY = findStart(grid)

    expected = 21
    _, actual = processBeam(grid, startX, startY)
    try:
        assert expected == actual
    except AssertionError:
        print(f"Expected {expected}, but got {actual}")

test()