# Exercise 6
from homework_winter2024.templates.exercise_3.ex3 import sort_2
"""
sort_2 is from exercise 3.
"""


def sliding_window_median(a_list:list[int], k:int)->list[float]:
    '''
    Function that calculates the median of a list of integers using a sliding window of length k.
    '''

    def bubble_sort_in_place(a_list):
        """
        bubble sort
        use sort_2
        """
        n = len(a_list)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                num = a_list[j:j + 2]
                sort_2(num)
                a_list[j:j + 2] = num

    n = len(a_list)
    result = [0] * (n - k + 1)

    for i in range(n - k + 1):
        subcopy = a_list[i:i + k]  # copy

        bubble_sort_in_place(subcopy) # use bubble_sort_in_place( )
         # get the median
        if k % 2 == 1:
            median = subcopy[k // 2]
        else:
            median = subcopy[(k // 2) - 1]

        result[i] = median

    return result
"""
What is the time complexity of your function in the worst case? Answer in a comment in the
template.

In the worst case,the complexity of the function is O((n-k+1)*k**2).
"""

print("""
Happy 2025!!!
Happy 2025!!!
Happy 2025!!!""")