letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(letters.append('AA'))  # it adds the specified element ('AA') to the end of the list. The append() method modifies the original list and does not return a new list.
print(letters) #it lazy one
#it changes the original list and does not return a new list, so when you print letters.append('AA'), it will print None because the append() method does not return anything. However, when you print letters after appending 'AA', it will show the updated list with 'AA' added at the end.
grocery = [
    'Rice',
    'Eggs',
    'Milk',
    'Bread',
    'Hotdog',
    'Chicken',
    'Tomato',
    'Onion',
    'Cheese',
    'Cooking Oil'
]

grocery.insert(0, 'Start') #it inserts the specified element ('Start') at the specified index (0 in this case). The insert() method modifies the original list and does not return a new list.
grocery.insert(5, 'Pasta')
print(grocery)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix.append([10, 11, 12]) #it adds the specified element ([10, 11, 12]) to the end of the list. The append() method modifies the original list and does not return a new list.
matrix.insert(0, [1, 2, 4])
print(matrix)

num = [3, 12, 7, 1, 15, 9, 4, 6, 10, 2]
num.clear() #it removes all elements from the list, resulting in an empty list. The clear() method modifies the original list and does not return a new list.
print(num)

let = ['a', 'b', 'a']
let.remove('a')
removed = let.pop()
print(let) #IT removes specific value
print('The remove item :', removed) #it return the value

