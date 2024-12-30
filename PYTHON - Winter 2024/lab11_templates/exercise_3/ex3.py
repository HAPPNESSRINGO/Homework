#%% Exercise 3 Part A
def sort_2(a_list:list[int])->list[int]:
    '''
    Function that sorts a list of exactly two elements in place.
    '''
    for i in range(len(a_list)-1):
        if a_list[i] > a_list[i+1]:
            a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    return a_list
        
#%% Exercise 3 Part B
def sort_3(a_list:list[int])->list[int]:
    '''
    Function that sorts a list of exactly three elements in place.
    '''
    sort_2(a_list)
    sort_2(a_list)
    return a_list

print("""
Happy 2025!!!
Happy 2025!!!
Happy 2025!!!""")