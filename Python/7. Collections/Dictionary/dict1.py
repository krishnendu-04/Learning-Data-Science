# student = {
#     "name":"krishnendu",
#     "age":23,
#     "college":"SCMS School of Engineering & Technology",
# }
# print(student)
# print(type(student))


# #Different datatype as values
# student = {
#     "name":"krishnendu",
#     "age":23,
#     "college":"SCMS School of Engineering & Technology",
#     "cgpa":8.08,
#     "passed":True,
#     "subjects": ["Python","R","Big Data","Data Analytics","Data structure"],
#     "Departments":{2,6,8},
#     "Team":("Blue","White","Green")
# }
# print(student)

# #Different datatype as keys
# dictionary1 = {
#     "subject":"Python",
#     20:"Red",
#     97.5:"High score",
#     True:1
# }
# print(dictionary1)

# #Duplicates values
# dict2 = {
#     "name":"anu",
#     "name1":"anu"
# }
# print(dict2)

# #Duplicates keys
# dict2 = {
#     "name":"anu",
#     "name":"fidha"
# }
# print(dict2)


# #accessing elements in a dictionary 

# #1. using keys
# student = {
#     "name":"krishnendu",
#     "age":23,
#     "college":"SCMS School of Engineering & Technology",
# }
# print(student["name"])
# print(student["age"])
# print(student["college"])
# #print(student[0]) ----> Not index based, ERROR
# #print(student["number"]) ----> key not present in dictionary, ERROR

# # 2. get()
# student = {
#     "name":"krishnendu",
#     "age":23,
#     "college":"SCMS School of Engineering & Technology",
# }
# print(student.get("name"))
# print(student.get("age"))
# print(student.get("college"))
# print(student.get("number")) #if key doesnt exist ---> None
# print(student.get("number","Not available")) #we can set default value

# #[] vs get()
# #[] gives error if key not present, not index based
# #get() returns None if key not present, set default value instead of none

# #Adding an element

# # 1. dicitonary["key"] = "value"
# dictionary1 = {
#     "name":"anu",
#     "mark":89.7,
# }
# dictionary1["passed"] = True
# print(dictionary1)

# #Updating a value
# dictionary1["mark"] = 75
# print(dictionary1)

# # if key already exists ----> updates the value
# # if key doesnt exist ----> adds a new key-value pair
# dictionary1["number"] = 75
# print(dictionary1)

# # 2. using update() - used to add or update one or more key value pairs
# dictionary2 = {
#     "name":"anu",
#     "mark":89.7,
# }
# dictionary2.update({
#     "roll_num":42,
#     "mark1": 90
# })
# print(dictionary2)

# Removing elements

#1. pop() - remove elements using keys

student = {
    "name":"parvathy",
    "age":20,
    "mark":98,
    "college":"SSET"
}
print(student)
student.pop("age")
print(student)

#2. popitem() - remove last inserted key-value pair
student.popitem()
print(student)

#3. del - used to delete a specific key-value pair
del student["mark"]
print(student)

# 4. clear - remove all elements from the dictionary
student.clear()
print(student)


student = {
    "name":"parvathy",
    "age":20,
    "mark":98,
    "college":"SSET"
}
print("age" in student)