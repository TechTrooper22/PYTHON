# Tuple is immutable i.e. can not be modified

tup = (1,)  # method to define single element with ",", compulsory.   
print(tup)

# writimg "," after every element is good practice
tup1 = (1,2,3,4,5,)
print(tup1)

'''
# Slicing
marks = (88,78,68,97,68,75,95,68,)
print(marks[1:3])

# .index(ele) - returns index of first occurrence.
print(marks.index(68))

# .coumt(ele) - counts occurrence
print(marks.count(68))
'''

# WAP to count the number of student with the "A" grade in the following tuple.
tup = ("C", "A", "D", "A", "A", "B", "B", "A",)
print("Total A grade:",tup.count("A"))