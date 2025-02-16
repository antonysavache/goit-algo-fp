def greedy_algorithm(items, budget):
    """
    Greedy approach to maximize calories within budget
    Returns (selected_items, total_cost, total_calories)
    """
    # Calculate value (calories per cost) for each item
    value_ratio = {
        item: data["calories"] / data["cost"]
        for item, data in items.items()
    }

    # Sort items by value ratio
    sorted_items = sorted(items.keys(), key=lambda x: value_ratio[x], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    # Select items until budget is exhausted
    for item in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    """
    Dynamic programming approach to maximize calories within budget
    Returns (selected_items, total_cost, total_calories)
    """
    # Create DP table
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Convert items to list for indexing
    items_list = list(items.items())

    # Fill DP table
    for i in range(1, len(items) + 1):
        item_name, item_data = items_list[i-1]
        for w in range(budget + 1):
            if item_data["cost"] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][w - item_data["cost"]] + item_data["calories"]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # Backtrack to find selected items
    selected_items = []
    total_calories = dp[len(items)][budget]
    total_cost = 0
    w = budget

    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item_name, item_data = items_list[i-1]
            selected_items.append(item_name)
            w -= item_data["cost"]
            total_cost += item_data["cost"]

    return selected_items, total_cost, total_calories

def compare_algorithms(items, budget):
    """Compare results of both algorithms"""
    print(f"\nComparing algorithms with budget: ${budget}")
    print("-" * 50)

    # Run greedy algorithm
    greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    print("\nGreedy Algorithm Results:")
    print(f"Selected items: {greedy_items}")
    print(f"Total cost: ${greedy_cost}")
    print(f"Total calories: {greedy_calories}")

    # Run dynamic programming
    dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming Results:")
    print(f"Selected items: {dp_items}")
    print(f"Total cost: ${dp_cost}")
    print(f"Total calories: {dp_calories}")

    # Compare results
    print("\nComparison:")
    print(f"Difference in calories: {dp_calories - greedy_calories}")
    if dp_calories > greedy_calories:
        print("Dynamic Programming found a better solution!")
    elif dp_calories < greedy_calories:
        print("Greedy Algorithm found a better solution!")
    else:
        print("Both algorithms found equally good solutions!")

# Test the implementation
def run_tests():
    # Sample food items
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # Test with different budgets
    budgets = [50, 100, 150]
    for budget in budgets:
        compare_algorithms(items, budget)

if __name__ == "__main__":
    run_tests()