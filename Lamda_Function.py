multiple = lambda x: x * 2
print(multiple(2)) #it will print the result of multiplying 2 by 2 which is 4

addlambda = lambda x, y: x + y #it is a lambda function that takes two arguments x and y and returns their sum
print(addlambda(3, 5)) #it will print the result of adding 3 and 5 which is 8

check = lambda i: i in 'python' #it is a lambda function that checks if the input i is in the string 'python'
print(check('p')) #it will print True because 'p' is in 'python'

prices = ['$10', '$20', '$30', '$40', '$50']

p = '$10' #it is a string that represents the dollar sign
print(list(map(lambda x: x.replace('$', ''), prices))) #it will print the result of replacing the dollar sign with an empty string which is '10'

price = [100, 30, 500, 200, 50 ]
print(list(filter(lambda x: x >= 100, price))) #it will print the result

students = [('Alice', 85), ('Bob', 90), ('Charlie', 75), ('David', 80), ('Eve', 95)]
print(list(filter(lambda x: x[1] >= 80, students))) #it will print the list
print (students[2][1] >= 80) #it will print True because the score of Charlie is 75 which is less than 80