info = {
    "key" : "value", 
    "int" : 21,
    "float" : 20.99,
    "char" : "t",
    "bool" : True,
    "list" : [1, 2, 3, 4, 5],
    "tuple" : (1,)
}
print(info)
print(info["list"])
print(info["tuple"])
info["int"] = 22
print(info)


# Nested Dictionary 
student = {
    "name" : "Tejas",
    "subject" : {
        "Physics" : 89,
        "Chemistry" : 84,
        "Mqathematics" : 90
    },
    "Age" : 21
}
print(student)
print(student["subject"])
print(student["subject"]["Physics"])


# .key() - return all keys
print(student.keys())

# .values() - return all values
print(student.values())

# .items() - returns all (key, val) pairs as a tuples
print(student.items())

# .get("key") - returns the key according to value
print(student.get("name"))  # same as student["name"]

# .update()
student.update({"Gender" : "Male"})
student.update({"name" : "Yadnyesh"})   # key alread exist, changing value
print(student)

print(len(student))


