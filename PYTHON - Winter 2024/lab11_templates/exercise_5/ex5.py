# Exercise 5
def get_missing_characters(sentence:str)->list[str]:
    '''
    Function that returns a list of the missing characters in the sentence.
    '''
    letters ="abcdefghijklmnopqrstuvwxyz" # 26 English letters
    missing_letters = []
    for letter in letters:
        if letter not in sentence:
            missing_letters = missing_letters + [letter]
    return missing_letters

print("""
Happy 2025!!!
Happy 2025!!!
Happy 2025!!!""")