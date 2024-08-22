# Lists are mutable i.e. can be modified

student = ["Tejas", 21, "Mohpa", "Male"]
# print(student)
# print(student[0])
# student[0] = "Yadnyesh"
# print(student)

marks = [87, 64, 33, 95, 76]

# Slicing
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])



# .append(ele) - adds element in the end
marks.append(95)
print(marks)

# .sort() - sorts in ascending order
marks.sort()
print(marks)

# .sort(reverse = True) - sort in descending order
marks.sort(reverse = True)
print(marks)

# .reverse() - reverse list
marks.reverse()
print(marks)

# .insert(idx, ele) - insert element at that index
marks.insert(2, 88)
print(marks)

# .remove(ele) - removes first occurrence of element
marks.remove(64)
print(marks)

# .pop(idx) - removes element at index
marks.pop(4)
print(marks)

# .copy() - copies the element in new variable.
mark = marks.copy()


# movies = []
# mov1 = input("Enter movie nmae: ")
# mov2 = input("Enter movie nmae: ")
# mov3 = input("Enter movie nmae: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# movies = []
# movies.append(input("Enter 1st movie nmae: "))
# movies.append(input("Enter 2nd movie nmae: "))
# movies.append(input("Enter 3rd movie nmae: "))
# print(movies)

# WAP to check if a list contains a palindrome of elements.
l1 = [1, 2, "one", 3, 2, 1]
l2 = l1.copy()
l2.reverse()
if(l2 == l1):
    print("It is Palindrome")
else:
    print("It is not Palindrome")
