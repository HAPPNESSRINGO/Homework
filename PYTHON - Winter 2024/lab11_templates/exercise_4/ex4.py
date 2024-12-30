# Exercise 4:

from homework_winter2024.templates.exercise_2.ex2 import sorted_by_map
"""
Ex2's show time!!!
"""

def sort_by_profit(products:list[str], prices:list[float], costs:list[float]):
    '''
    Function that sorts the 3 lists by ascending profit using selection sort
    '''
    n = len(products)
    profits = [0] * n
    for i in range(n):
        profits[i] = prices[i] - costs[i]
    indexes = list(range(n))

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if profits[indexes[j]] < profits[indexes[min_idx]]:
                min_idx = j
        indexes[i], indexes[min_idx] = indexes[min_idx], indexes[i]

    map_list = [0] * n
    for new_pos in range(n):
        old_pos = indexes[new_pos]
        map_list[old_pos] = new_pos

    sorted_products = sorted_by_map(products, map_list)
    sorted_prices = sorted_by_map(prices, map_list)
    sorted_costs = sorted_by_map(costs, map_list)
    for i in range(n):
        products[i] = sorted_products[i]
        prices[i] = sorted_prices[i]
        costs[i] = sorted_costs[i]

print("""
Happy 2025!!!
Happy 2025!!!
Happy 2025!!!""")

