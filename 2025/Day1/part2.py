"""
There is a combination lock with numbers 0 - 99
You have a set of instructions that tell you how to turn the lock (i.e R30, L66)
Turning the lock Left past 0, will go to 99. Turning the lock Right past 99, will go to 0

~~The answer is how many times the combination reaches 0 after an instruction~~
You realize this is wrong. The answer is actually how many times the dial passes over or reaches.
For example, R1000 will pass over 0 several times before ending its rotation

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
        
        q, r = divmod(num, 100)
        count += q

        if (dir == "R"):
            k = 100 - dial if dial != 0 else 100

            if (dial + r >= 100):
                count += 1

            dial = (dial + r) % 100

        if (dir == "L"):
            k = dial if dial != 0 else 100

            if (dial - r <= 0):
                count += 1

            dial = (dial - r) % 100
        
        # while (num > 0):
        #     if (dir == "R"):
        #         dial = (dial + 1) % 100
            
        #     elif (dir == "L"):
        #         dial = (dial + (100 - 1)) % 100
            
        #     if (dial == 0):
        #         count += 1
            
        #     num -= 1

print(f"Correct answer: 7199")
print(f"Number of zeroes: {count}")
