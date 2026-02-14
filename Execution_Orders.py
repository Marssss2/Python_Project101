x=5
y=8
z=6

print(x==5 or y>5 and z<4) # it will return true because all conditions are true.
# and operator has higher precedence than or operator, so it will evaluate y>5 and z<4 first, which is true, and then it will evaluate x==5 or true, which is also true.

print((x==5 or y>5) and z<4) # it will return true because all conditions are true.
# parentheses have higher precedence than and operator, so it will evaluate x==5 or y>5 first, which is true, and then it will evaluate true and z<4, which is also true.

