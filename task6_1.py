"""Реалізація алгоритмів, якщо страви не можуть повторюватись"""

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]
    
    return selected_items, total_calories, total_cost

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    # Створюємо таблицю для зберігання максимальних калорійностей при різних бюджетах
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[item_names[i - 1]]["cost"] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - items[item_names[i - 1]]["cost"]] + items[item_names[i - 1]]["calories"]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних предметів
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]["cost"]

    total_calories = dp[n][budget]
    total_cost = budget - w

    return selected_items, total_calories, total_cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Selected items: {selected_items}")
print(f"Total calories: {total_calories}")
print(f"Total cost: {total_cost}")

selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print(f"Selected items: {selected_items}")
print(f"Total calories: {total_calories}")
print(f"Total cost: {total_cost}")