# 'is' is == used to check if two variables refer to the same object in memory, while '==' is used to check if the values of two variables are equal.   
# and 'is not' is same as != but it checks for identity rather than equality. It returns true if the variables do not refer to the same object in memory, and false if they do. 


# 'is' is used to check if two variables refer to the same object in memory.
a = [1, 2, 3]
b = [1, 2, 3]
a == b # it will return true because a and b have the same content.
print(a == b) # it will return true because a and b have the same content.
print(a is b) # it will return false because a and b are different objects in memory    

y = 10
z = 10
print(y == z) # it will return true because y and z have the same value.
print(y is z) # it may return true because small integers are cached by Python, so y and z may refer to the same object in memory. However, this behavior is an implementation detail and should not be relied upon in general.

d = [1, 2, 3]
e = d
print(d == e) # it will return true because d and e have the same content.
print(d is e) # it will return true because d and e refer to the same object in memory.