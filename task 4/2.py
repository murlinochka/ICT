import random

def roll():
    return (random.randint(1,6)+random.randint(1,6))

def count(amount, ):
    count_ = 0

    for i in range(1, amount+1):
        if roll() == 3:
            count_ += 1
    return count_

print(roll())