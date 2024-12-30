import time, random
from typing import List

from colored_text import colored_text_with_bg, BG_GREEN, BG_RED


def colored_step(a_list: List[int], min_idx:int, unsorted_idx:int) -> str:
    '''
    Function that returns a string composed of all the elements in
    a_list with their appropriate color code:
        Minimum element in red background and black text
        Unsorted elements are uncolored
        Sorted elements in green background and black text
        
    min_idx - position of the minimum element in the unsorted list.
    unsorted_idx - position of the first unsorted element from the left.
    '''
    result = ''
    for i in range(len(a_list)):
        elem = a_list[i]
        elem_string = ' ' + str(elem) + ' '
        if i < unsorted_idx:
            elem_string = colored_text_with_bg(elem_string.strip(), BG_GREEN)
        elif i == min_idx:
            elem_string = colored_text_with_bg(elem_string.strip(), BG_RED)

        result += elem_string + "😋" # emoji is better than space. Happy 2025!!!
        """
        🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪
        Happy 2025!!!
        Happy 2025!!!
        Happy 2025!!!
        """


    return result

# You can uncomment this code if you want to test your implementation
print(colored_step([3,1,4,0,2], 3, 2)) # should print correctly colored string

def steps_of_selection_sort(a_list: List[int]) -> List[str]:
    '''
    Function that returns a list of steps of the selection sort algorithm.
    Each step is a string that represents the current state of the list,
    with the corresponding color codes.
    '''

    def find_min_index(a_list: List[int], start: int, end: int) -> int:
        '''
        Function to find the minimum index
        '''
        min_idx = start
        for i in range(start + 1, end):
            if a_list[i] < a_list[min_idx]:
                min_idx = i
        return min_idx

    result = []
    n = len(a_list)
    for unsorted_idx in range(n - 1):
        # Use find_min_index
        min_idx = find_min_index(a_list, unsorted_idx, n)
        a_list[min_idx],a_list[unsorted_idx] =  a_list[unsorted_idx],a_list[min_idx]
        step_string = colored_step(a_list, min_idx=unsorted_idx, unsorted_idx=unsorted_idx + 1)
        result.append(step_string)

    # Add the now sorted, all green, final step:
    result.append(colored_step(a_list, n, n))

    return result

def show_process_of_selection_sort(a_list: List[int], tick=0.5) -> None:
    '''
    Function that prints a visualization of the selection sort algorithm
    by printing each step of the algorithm with a delay of tick seconds.
    '''
    steps = steps_of_selection_sort(a_list)
    for step in steps:
        print(step)
        time.sleep(tick)

# You can uncomment this code if you want to test your implementation
random_list = random.sample(range(1, 100), 10)
show_process_of_selection_sort(random_list)

print("""
Happy 2025!!!
Happy 2025!!!
Happy 2025!!!""")
