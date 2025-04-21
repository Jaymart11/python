import random

numberOfStreaks = 0

for experiment in range(10000):
    streak = 1
    prev = random.choice(["H", "T"])

    for _ in range(99):
        current = random.choice(["H", "T"])
        if current == prev:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                break  # stop after finding a streak
        else:   
            streak = 1  # reset streak
        prev = current

print('Chance of streak: %s%%' % (numberOfStreaks / 100))