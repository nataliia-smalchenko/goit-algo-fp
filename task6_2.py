"""Реалізація алгоритмів, якщо страви можуть повторюватись"""

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = {}

    while total_cost <= budget:
        added = False
        for item, details in sorted_items:
            if total_cost + details["cost"] <= budget:
                selected_items[item] = selected_items.get(item, 0) + 1
                total_cost += details["cost"]
                total_calories += details["calories"]
                added = True
                break  # Йдемо до початку циклу, щоб знову пройти від найкращого варіанту
        if not added:
            break  # Якщо жодна страва не додалась, виходимо з циклу
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    # Створюємо таблицю для зберігання максимальних калорійностей при різних бюджетах
    dp = [0] * (budget + 1)

    # Заповнюємо таблицю dp
    for w in range(1, budget + 1):
        for i in range(n):
            if items[item_names[i]]["cost"] <= w:
                dp[w] = max(dp[w], dp[w - items[item_names[i]]["cost"]] + items[item_names[i]]["calories"])

    # Відновлення вибраних предметів
    selected_items = {}
    w = budget
    while w > 0:
        for i in range(n):
            if items[item_names[i]]["cost"] <= w and dp[w] == dp[w - items[item_names[i]]["cost"]] + items[item_names[i]]["calories"]:
                selected_items[item_names[i]] = selected_items.get(item_names[i], 0) + 1
                w -= items[item_names[i]]["cost"]
                break

    total_calories = dp[budget]
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