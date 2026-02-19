numbers = [5, 12, 7, 20, 33, 8, 14, 1, 27, 19]
list = [1,2,3]

print(list == numbers)
print("Numbers in the list:", numbers)
print("Length of the list:", len(numbers))
print("Sum of all numbers:", sum(numbers))
print("Average of numbers:", sum(numbers) / len(numbers))
print('All:', all(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Sorted numbers:", sorted(numbers))
print("Unique numbers:", set(numbers))
print(f'{numbers.count(7)} occurrences of the number 7')

print('Any:', any(numbers))#it checks if at least one element in the list is truthy (non-zero in this case). Since all numbers are non-zero, it returns True.
# any will be false if any value will be a string or any other 

print('Index', numbers.index(20))#it returns the index of the first occurrence of the specified value (20 in this case). If the value is not found, it raises a ValueError.
print(20 in numbers)