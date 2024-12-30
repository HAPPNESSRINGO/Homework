# Exercise 1
def is_sorted(a_list:list) -> bool:
    '''
    Function that takes a list of integers and returns True if the list is sorted in ascending order and False otherwise.
    '''
    for i in range(len(a_list) - 1):
        if not a_list[i] <= a_list[i + 1]:
            return False
    return True
"""
What is the time complexity of your function in the worst case? Answer in a comment in the
template.

In the worst case,the complexity of the function is O(n).
"""

print("""
Happy 2025!!!
Happy 2025!!!
Happy 2025!!!""")