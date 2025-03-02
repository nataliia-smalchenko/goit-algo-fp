import numpy as np
import matplotlib.pyplot as plt


def roll_dice():
    """Отримання результату підкидання 2-х кубиків"""
    return np.random.randint(1, 7) + np.random.randint(1, 7)

def simulate_dice_rolls(trials):
    """Отримання результатів випробуваня, кількість випробувань - trials"""
    sums = np.zeros(11)  # Індекси від 0 до 10 відповідають сумам від 2 до 12
    for _ in range(trials):
        roll_sum = roll_dice()
        sums[roll_sum - 2] += 1

    probabilities = (sums / trials) * 100
    return probabilities

def plot_probabilities(probabilities):
    """Побудова графіку ймовірностей"""
    sums = range(2, 13)
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probabilities, color='skyblue')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Імовірність')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.grid(True)
    plt.show()

def show_probabilities_table(probabilities):
    """Функція для відображення ймовірностей"""
    print("╭──────────┬───────────────╮")
    print("│   Сума   │  Ймовірність  │")
    print("├──────────┼───────────────┤")
    for sum_value, probability in zip(range(2, 13), probabilities):
        print(f"│{str(sum_value).center(10)}│{str(round(probability, 2)).center(15)}│")
        if sum_value < 12:
            print("├──────────┼───────────────┤")
        else:
            print("╰──────────┴───────────────╯")


# Симуляція кидків кубиків
trials = 1_000_000
probabilities = simulate_dice_rolls(trials)

# Виведення ймовірностей сум
show_probabilities_table(probabilities)

# Побудова графіку
plot_probabilities(probabilities)