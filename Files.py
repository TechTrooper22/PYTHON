'''
'r' - open for reading (default)
'w' - open for writing, truncating the files first
'x' - create  a new file & open it for writing
'a' - open for writing, appending to the end of the file if exits
'b' - binary mode
't' - text mode
'+' - open a disk file for updating
'''

'''
f = open("files.txt", "r")
# data = f.read()
# print(data)

# data = f.read(5)  # print first 5 characters
# print(data)    

# line1 = f.readline()    # reads line one at a time.
# print(line1)
# line2 = f.readline()    
# print(line2)

f.close()
'''

'''
f = open("files.txt", "w")
f.write("I want to learn Jawa Script")
f.close() 
# open files.txt to view the result.
'''

'''
f = open("files.txt", "a")
f.write("After that I will start ReactJS")
f.close() 
# open files.txt to view the result.
'''

'''
# Anther Method -->
with open("files.txt", "r") as f:
    print(f.read())
'''

'''
f = open("wwe.txt", "w")    # Created file from here
f.write("WWE is fake but still I am watching it.")
f.close()
'''

'''
# Syntax to delete a file
import os
os.remove("wwe.txt")
'''

'''
# Create a new file & add following data
with open("practice.txt", "w") as t:
    t.write("Hi eyeryone\nWe are learning File I/O\nusing Java\nI like programming in Java.")
    t.close()
'''

'''
# replace all occurrences of "Java" with "Python" in above file

with open("practice.txt", "r") as t:
    data = t.read()
    newData = data.replace("Java", "Python")
print(newData)
with open("practice.txt", "w") as t:
    t.write(newData)    
'''

'''
# check 'learning' is in the file or not

word = "learning"
with open("practice.txt", "r") as t:
    data = t.read()
    if(data.find(word) != -1):  # we can also write it as 'if(word in data)'
        print("Found")
    else:
        print("Not Found")
'''

'''
# Count even numbers in a file which are seperated by ','

count = 0
with open("number.txt", "r") as t:
    data = t.read()
    num = data.split(",")
    for val in num:
        if (int(val)%2 == 0):
            count += 1
print(count)
'''