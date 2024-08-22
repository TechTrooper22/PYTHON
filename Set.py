# Each elementis unique & immutable.

set = {1, 2, 3, 3, 3, 4, 5, 5, 6}
print("Set:", set)

print("Length:",len(set))


# .add(ele) - add an element to the set
set.add(7)
print("Set:", set)

# .remove(ele)  
set.remove(7)
print("Set:", set)

#.clear() - empties the set
# set.clear()
# print("Set:", set)

# .pop() - removes random value
set.pop()
print("Set:", set)


# .union(newSet)
set1 = {1,3,5,7,9}
set2 = {2,4,6,8,0}
print("Union of two sets: ", set1.union(set2))

# .intersection(set)
set3 = {11,22,33,44}
set4 = {22,44,66,88}
print("Intersection of two sets:", set3.intersection(set4))


