letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',]
letters[1] = 'BB' #it changes the value of the element at index 1 to 'BB'. This modifies the original list and does not return a new list.
letters[0] = 'AA' #it changes the value of the element at index 0 to 'AA'. This modifies the original list and does not return a new list.
print(letters)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20 #it changes the value of the element at index [0][1] (which is 2) to 20. This modifies the original list and does not return a new list.
matrix[1][1] = 50 #it changes the value of the element at index [1][0] (which is 4) to 40. This modifies the original list and does not return a new list.
print(matrix)