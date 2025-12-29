"""
There is a combination lock with numbers 0 - 99
You have a set of instructions that tell you how to turn the lock 
    (i.e R30 -> Right 30, L66 -> Left 66)

Turning the lock Left past 0, will go to 99. Turning the lock Right past 99, will go to 0

The answer is how many times the combination reaches 0 after an instruction

Note: The lock starts with the dial at 50
"""

count = 0

dial = 50
with open("input", "r") as f:
    while(True):
        inst = f.readline()

        if (not inst):
            break

        dir = inst[0]
        num = int(inst[1:])

        if (dir == "R"):
            dial = (dial + num) % 100
        
        elif (dir == "L"):
            dial = (dial + (100-num)) % 100
        
        if (dial == 0):
            count += 1
    

print(f"Number of zeroes: {count}")