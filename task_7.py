import random
import matplotlib.pyplot as plt


def simulate_dice_throws(num_throws):
    sums = [0] * 11  # Суми від 2 до 12 (індекси 0-10)

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums[dice_sum - 2] += 1  # Зміщення на 2

    probabilities = [count / num_throws for count in sums]
    return probabilities



probabilities = simulate_dice_throws(10000)
print("Dice probabilities:")
sums = list(range(2, 13))
for i in range(len(sums)):
    print(f"  sum {sums[i]} : {round(probabilities[i]*100,2)}%")
