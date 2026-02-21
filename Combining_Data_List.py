#Combining

letter = [ 'a', 'b', 'c']
numbers = [1, 2, 3]

combined = letter + numbers
print(combined) # it will print the combined list which contains both letters and numbers.

combined = [letter, numbers]
print(combined) # it will print a list of two lists, where the first list contains the letters and the second list contains the numbers.

letter.extend(numbers)
print(letter) # it will print the original letter list which has been modified to include the numbers as well.

comb = zip(letter, numbers,'Hii')
print(list(comb)) # it will print a list of tuples, where each tuple contains one element from the letter list and one element from the numbers list, paired together based on their positions in the original lists.

ids = [101,102,103]
names = ['Alice', 'Bob', 'Charlie']
combined = zip(ids, names)
print(list(combined)) # it will print a list of tuples, where each tuple contains one