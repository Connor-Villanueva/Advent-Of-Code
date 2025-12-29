"""
You are presented banks of batteries with their joltages
In the input, each row is a bank

You need to turn on exactly two batteries within each bank
The joltage that bank produces is equal to the number formed by the digits
    of the batteries you've turned on. (i.e 3 & 6 -> 36)

You need to find the largest possible joltage that each bank can produce

What is the largest possible total output joltage?
"""


def findBatteries(bank: list[int]) -> int :
    first = bank.index(max(bank[:-1]))
    second = bank.index(max(bank[first+1:]))

    return int(str(bank[first]) + str(bank[second]))

joltage = 0
with open("input", "r") as f:
    while (True):
        data = f.readline().rstrip()
        if (not data):
            break

        bank = [int(i) for i in data]
        joltage += findBatteries(bank)

print(f"Max total voltage: {joltage}")
        