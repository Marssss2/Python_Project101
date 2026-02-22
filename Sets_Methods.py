a = {10, 20, 30, 40}

a.add(50)
print(a) #it means that 50 is already present in the set and it will not be added again

a.update([60, 70, 80])
print(a) #it means that 60, 70, and 80 are added to the set

a.discard(20)
print(a) #it means that 20 is removed from the set

b = {10, 30, 50, 70, 90}
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a.difference(b))