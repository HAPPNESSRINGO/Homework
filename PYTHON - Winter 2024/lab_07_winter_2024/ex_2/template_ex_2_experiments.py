#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python TC 7 

@author: Yiyang Wang 999028285
python-winter-2024
"""

from template_ex_2_forest_burnt import dynamics
import matplotlib.pyplot as plt


def experimenting_prob_sprouts(forest_size=100, repeat=50, prob_lightning=0.02):
    prob_max = 0  # will have the p_sprout_value that match the maximum mean
    mean_max = 0  # will have the maximum mean value of all the prob_sprout_values

    step = 0.1
    p = 0
    while p <= 1.0:
        # Run dynamics with the current prob_sprouts value
        results = dynamics(forest_size, repeat, p, prob_lightning)
        mean_result = sum(results) / len(results)  # Calculate the mean population

        # Update prob_max and mean_max if a new maximum is found
        if mean_result > mean_max:
            prob_max = p
            mean_max = mean_result

        p += step

    return prob_max, mean_max


def experimenting_prob_sprouts_plot(forest_size=100, repeat=50, prob_lightning=0.02):
    prob = []  # Accumulate all the values of all the used prob_sprouts in order
    mean = []  # Accumulate all the mean results of all the repetitions
    step = 0.01
    p = 0
    while p < 1.0:
        res = dynamics(forest_size, repeat, p, prob_lightning)
        average = sum(res) / len(res)
        mean.append(average)
        prob.append(p)
        p += step

    plt.title("Performance of the prob_sprouts")
    plt.xlabel("p-values", fontsize=16, color="blue")
    plt.ylabel("Yearly Mean", fontsize=16, color="blue")
    plt.plot(prob, mean)
    plt.show()

if __name__ == "__main__":
    # Find the best prob_sprouts value and its mean
    best_prob, best_mean = experimenting_prob_sprouts()
    print(f"The best prob_sprouts value: {best_prob}, with a mean of: {best_mean}")

    # Generate the plot
    experimenting_prob_sprouts_plot()
