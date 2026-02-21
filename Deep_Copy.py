import copy
original = ['a', 'b', 'c', 'd']
original_copy = copy.deepcopy(original) #it creates a deep copy of the original list. The deepcopy() function from the copy module creates a new list that is a copy of the original list, including any nested lists.
original_copy.append('e') #it adds 'e' to the end of the original_copy list. This does not affect the original list.
original.pop()
print(f'Original: {original}')
print('Copy:', original_copy)   