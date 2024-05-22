items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    print(sorted_items)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]

    return selected_items, total_calories



budget = 100

greedy_selected_items, greedy_total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_selected_items)
print("Total calories:", greedy_total_calories)

dp_selected_items, dp_total_calories = dynamic_programming(items, budget)
print("\nDynamic Programming Algorithm:")
print("Selected items:", dp_selected_items)
print("Total calories:", dp_total_calories)
