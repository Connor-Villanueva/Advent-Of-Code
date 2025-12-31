"""
You enter a teleporter hub and decide to step onto a large teleporter pad.
Suddently, you find yourself in an unfamilar room. The teleporter pad appears to be
leaking magic smoke.

After connecting some diagnostic tools, you find there is an issue with the tachyon manifolds.
You locate a diagram of the tachyon manifold (the input).

Tachyon beams pass start at (S).
They are free to pass through empty spaces (.)
~~If a beam encounters a splitter (^), the beam is stopped 
    and continues on from the immediate left and right~~

You realize this is actually a quantum tachyon manifold.
Only a single tachyon particle is sent through the manifold, taking both the left and right paths.
The manual recommends the many-world interpretation, in which when a particle encounters a splitter, time itself
    is split.

How many timelines are active after a single particle completes all of its possible journeys through the manifold?

"""

# No recursion? (This could probably be cleaned up, but it works!)
def processBeam(grid, startX : int, startY: int):
    grid[startY][startX] = 1

    for y in range(startY+1, len(grid)):
        for x in range(len(grid[y])):
            if (grid[y][x] == "^" and grid[y-1][x] != "."):
                if (grid[y][x-1] == "."):
                    grid[y][x-1] = grid[y-1][x]
                else:
                    grid[y][x-1] += grid[y-1][x]
                
                if (grid[y][x+1] == "."):
                    grid[y][x+1] = grid[y-1][x]
                else:
                    grid[y][x+1] += grid[y-1][x]

            elif (grid[y][x] == "."):
                if (grid[y-1][x] != "^"):
                    grid[y][x] = grid[y-1][x]
            
            else:
                if (grid[y-1][x] != "." and grid[y-1][x] != "^"):
                    grid[y][x] += grid[y-1][x]
    count = 0
    for x in range(len(grid[-1])):
        if (grid[-1][x] != "."):
            count += int(grid[-1][x])
    
    return count


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

    expected = 40
    actual = processBeam(grid, startX, startY)
    try:
        assert expected == actual
    except AssertionError:
        print(f"Expected {expected}, but got {actual}")

test()