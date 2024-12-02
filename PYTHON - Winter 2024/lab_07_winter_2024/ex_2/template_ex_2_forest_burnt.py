#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python TC 7 

@author: Yiyang Wang 999028285
python-winter-2024
"""
import random


def empty_forest(size):
    return [0] * size


def random_event(prob):
    """
    True if the event occurs, False otherwise.
     """
    return random.random() < prob


def sprouts(forest, prob_sprouts):
    #Modifies the forest in-place
    for i in range(len(forest)):
        if forest[i] == 0 and random_event(prob_sprouts):
            forest[i] = 1


def how_many_survived(forest):
    """
 The number of surviving trees (state 1) in the forest.
    """
    return forest.count(1)


def lightning(forest, prob_lightning):
    """
        Modifies the forest in-place.
     """
    for i in range(len(forest)):
        if forest[i] == 1 and random_event(prob_lightning):
            forest[i] = -1



def spread(forest):
    new_forest = forest[:]  # Make a copy of the forest

    # Pass 1: Spread fire from left to right
    for i in range(1, len(forest)):
        if forest[i - 1] == -1 and forest[i] == 1:
            new_forest[i] = -1

    # Pass 2: Spread fire from right to left
    for i in range(len(forest) - 2, -1, -1):
        if forest[i + 1] == -1 and forest[i] == 1:
            new_forest[i] = -1

    # Update the original forest
    forest[:] = new_forest



def cleaning(forest):
    for i in range(len(forest)):
        if forest[i] == -1:
            forest[i] = 0





def dynamics(forest_size, repeat, prob_sprouts, prob_lightning):
    my_forest = empty_forest(forest_size)
    population = []

    for _ in range(repeat):
        sprouts(my_forest, prob_sprouts)
        lightning(my_forest, prob_lightning)
        spread(my_forest)
        cleaning(my_forest)

        population.append(how_many_survived(my_forest))

    return population

if __name__ == "__main__":
    # Forest size and number of yearly cycles
    forest_size = 100  # The number of cells in the forest
    repeat = 50  # The number of years to simulate

    # Different probabilities for lightning and tree sprouting
    prob_lightning_values = [0.1, 0.2, 0.3]  # Lightning probabilities
    prob_sprouts_values = [0.4, 0.6, 0.8]  # Sprouting probabilities

    # Display results for each combination of probabilities
    for prob_lightning in prob_lightning_values:
        for prob_sprouts in prob_sprouts_values:
            # Simulate the forest dynamics
            population = dynamics(forest_size, repeat, prob_sprouts, prob_lightning)

            # Calculate statistics
            max_population = max(population)  # Maximum number of surviving trees
            min_population = min(population)  # Minimum number of surviving trees
            avg_population = sum(population) / len(population)  # Average number of surviving trees

            # Print results
            print(f"Prob Lightning: {prob_lightning}, Prob Sprouts: {prob_sprouts}")
            print(f"Max survivors: {max_population}, Min survivors: {min_population}, Avg survivors: {avg_population:.2f}")
            print("-" * 40)
