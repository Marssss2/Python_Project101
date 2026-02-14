import math
#Measure Distance

print(abs(5-3)) #2

#Rounding Numbers
print(round(3.14159, 2)) #3.14
print(round(2.71828, 3)) #2.718
#2 is Ceiling and 1 is Floor
print(round(2.5)) #2
print(round(3.5)) #4    

price = 19.99999
print(math.ceil(price)) #20 #it will round the price up to the nearest integer, which is 20
print(math.floor(price)) #19 it will round the price down to the nearest integer, which is 19
print(round(price,2)) #20 it will round the price to 2 decimal places, which is 20.00 but since we are using round function it will give us 20 without the decimal places.
print(math.trunc(price)) #19 it will truncate the price to the nearest integer, which is 19 
print(int(price)) #19 it will convert the price to an integer, which is 19