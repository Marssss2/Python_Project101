original = ['a', 'b', 'c', 'd']
original_copy = original.copy() #it creates a shallow copy of the original list. The copy() method returns a new list that is a copy of the original list.
original_copy.append('e') #it adds 'e' to the end of the original_copy list. This does not affect the original list.
original.pop()
print(f'Original: {original}')
print('Copy:', original_copy)

#much safer to use copy() method to create a copy of the list instead of using assignment operator. This way, we can avoid unintended side effects on the original list when modifying the copy.

matrix = [[1, 2, 3],
          [3, 4, 5],
          [6, 7, 8,]
]
matrix_copy = matrix.copy() 
matrix.pop() #it removes the last element of the original list, which is [6, 7, 8]. This does not affect the copy of the list.
matrix_copy.append([9, 10, 11]) #it adds a new list [9, 10, 11] to the end of the copy of the list. This does not affect the original list. However, since the original list contains nested lists, modifying the nested lists in either the original or the copy will affect both lists because they reference the same nested lists in memory.
print(f'Original: {matrix}')
print('Copy:', matrix_copy)