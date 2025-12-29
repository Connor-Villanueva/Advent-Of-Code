"""
You are presented banks of batteries with their joltages
In the input, each row is a bank

~~You need to turn on exactly two batteries within each bank~~
You need to turn on exactly twelve batteries within each bank
The joltage that bank produces is equal to the number formed by the digits
    of the batteries you've turned on. (i.e 3 & 6 -> 36)

You need to find the largest possible joltage that each bank can produce

What is the largest possible total output joltage?
"""


def findBatteries(bank: list[int]) -> int :
    res = ""
    last_idx = -1

    print("Finding Battery: ", bank)
    for i in range(12):
        sub_bank = bank[last_idx + 1:-(11-i)] if i < 11 else bank[last_idx + 1:]

        battery = max(sub_bank)
        last_idx += sub_bank.index(battery) + 1

        # print(battery, last_idx, sub_bank)
        res += str(battery)

    # print(res)
    return int(res)

joltage = 0
with open("input", "r") as f:
    while (True):
        data = f.readline().rstrip()
        if (not data):
            break

        bank = [int(i) for i in data]
        joltage += findBatteries(bank)

# print("Expecting joltage: 3121910778619")
print(f"Max total joltage: {joltage}")
        