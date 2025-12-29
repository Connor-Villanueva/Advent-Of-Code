"""
You've fallen down a garbage chute and find yourself among some
cephalopods. The youngest needs help with her math homework.

Cephalopod math is similar to ours. Each problem is presented vertically
with the operation to be performed at the bottom of the each column.

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
        self.op = op

    def solve(self) -> int:
        match self.op:
            case "+":
                return sum(self.nums)
            case "*":
                return math.prod(self.nums)

def solveProblemSheet(sheet: list[list]):
    ret = 0
    for col in range(len(sheet[0])):
        pb = Problem()
        for row in range(len(sheet)):
            val = sheet[row][col]
            
            if (val != '*' and val != '+'):
                pb.addNum(val)
            else:
                pb.setOp(val)

        ret += pb.solve()
    
    return ret

def test():
    with open("test", "r") as f:
        problemSheet = []
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            s = line.split()
            problemSheet.append(s)

    expected = 4277556
    actual = solveProblemSheet(problemSheet)
    try:
        assert expected == actual
    except AssertionError:
        print(f"Expected {expected}, but got {actual}")

def main():
    with open("input", "r") as f:
        problemSheet = []
        while (True):
            line = f.readline().strip()

            if (not line):
                break

            s = line.split()
            problemSheet.append(s)
    
    print(solveProblemSheet(problemSheet))

# test()
main()