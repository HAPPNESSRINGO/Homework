#%% Exercise 2 Part A
def sorted_by_map(a_list:list[str], map:list[int])->list[str]:
    '''
    Function that returns a new list that is sorted based on the map list.
    '''
    new_list= a_list[:]
    for i in range(len(a_list)):
        new_list[map[i]]=a_list[i]
    return new_list




#%% Exercise 2 Part B
def sort_by_map(a_list:list[str], map:list[int]):
    '''
    Function that sorts a list in place based on the map list.
    '''
    new_list = a_list[:]
    for i in range(len(a_list)):
        new_list[map[i]] = a_list[i]
    for i in range(len(a_list)):
        a_list[i] = new_list[i]
