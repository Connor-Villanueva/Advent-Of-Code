"""
After figuring out the teleporter, you end up in an unfamilar place with a giant playground.
A group of elves are setting up a decoration project. They've suspended a large number of junction boxes.

They plan to connect the junction boxes with long strings of lights. 
When two junctions boxes are connected by a string of lights, electricity can pass between those two junction boxes.

The elves are trying to figure out which boxes to connect so that electricity can reach every junction box.
To save on string lights, the elves would like to connect pairs of junction boxes that are as close as possible.

After connecting two junction boxes, they become part of the same circuit.
Multiple junction boxes can be stringed together to form a bigger circuit.
"""
import math

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        self.distance_from_origin = math.sqrt(math.pow(x,2) + math.pow(y,2) + math.pow(z,2))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def getEuclideanDistance(p1: Point, p2: Point) -> int :
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2) + math.pow(p1.z - p2.z, 2))




def test():
    infile = "test"

    points = []
    with open(infile, "r") as f:
        while (True):
            line = f.readline().strip()

            if (not line):
                break

            x, y, z = line.split(",")
            points.append(Point(x,y,z))

    

        
test()