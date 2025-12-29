"""
You've fallen down a garbage chute and find yourself among some
cephalopods. The youngest needs help with her math homework.

~~Cephalopod math is similar to ours. Each problem is presented vertically
with the operation to be performed at the bottom of the each column.~~

Now the numbers in each problem are presented vertically. So instead of reading
each number from left to right, you now read them top-down.

To verify their work, the students are given the grand total of addind together
all of their answers.

Can you help the cephalopod student with her work?
"""
import math

class Problem():
    def __init__(self):
        self.nums : list[int] = []
        self.op : str = ""

    def addNum(self, num : str):
        self.nums.append(int(num))
    
    def setOp(self, op : str):
        if (self.op == ""):
            self.op = op
    
    def printProblem(self):
        print(self.nums, self.op)
    
    def solve(self):
        match self.op:
            case "+":
                return sum(self.nums)
            case "*":
                return math.prod(self.nums)


def solveProblemSheet(sheet : list[list]) -> int:
    ret = 0
    pb = Problem()
    for col in range(len(sheet[0])):
        curr = ""
        for row in range(len(sheet)):
            val = sheet[row][col]
            
            if (val != "*" and val != "+"):
                curr += val
            else:
                pb.setOp(val)

        if (curr.strip()):
            pb.addNum(curr)
        else:
            ret += pb.solve()
            pb = Problem()
    
    ret += pb.solve()
    
    return ret

        
        

def test():
    with open("test", "r") as f:
        problemSheet = []
        while (True):
            line = f.readline().rstrip("\n")

            if (not line):
                break

            problemSheet.append(list(line))

    expected = 3263827
    actual = solveProblemSheet(problemSheet)

    try:
        assert expected == actual
    except AssertionError:
        print(f"Expected {expected}, but got {actual}")

def main():
    with open("input", "r") as f:
        problemSheet = []
        while (True):
            line = f.readline().rstrip("\n")

            if (not line):
                break

            problemSheet.append(list(line))

    print(solveProblemSheet(problemSheet))

# test()
main()