ranndom_list = [1, False, 3, None, 5, '', 7, 8, None, 10]
filtered_list = list(filter(bool and None, ranndom_list)) #it will filter out all the falsy values from the list and return a new list with only the truthy values
print(filtered_list) #it will print the filtered list which contains only the truthy values

items = ['sql', 'python', '42', 'c++', '123']
filtered_items = list(filter(str.isalpha, items)) #it will filter out all the items that are not purely alphabetic and return a new list with only the alphabetic items
print(filtered_items) #it will print the filtered list which contains only the alphabetic items

for i in filter(str.isalpha, items):
    print(i) #it will print each item in the filtered list which contains only the alphabetic items