student1 = {
    "name":"krishnendu",
    "age":23,
    "college":"SCMS School of Engineering & Technology"
}
print(student1)
print(type(student1))

#-------------------------------------------------------------------------------------#

#Different datatype as values
student2 = {
    "name":"krishnendu",
    "age":23,
    "college":"SCMS School of Engineering & Technology",
    "cgpa":8.08,
    "passed":True,
    "subjects": ["Python","R","Big Data","Data Analytics","Data structure"],
    "Departments":{2,6,8},
    "Team":("Blue","White","Green")
}
print(student2)

#-------------------------------------------------------------------------------------#

#Different datatype as keys
dict1 = {
    "subject":"Python",
    20:"Red",
    97.5:"High score",
    True:1
}
print(dict1)

#-------------------------------------------------------------------------------------#

#Duplicates values
dict2 = {
    "name":"anu",
    "name1":"anu"
}
print(dict2)

#-------------------------------------------------------------------------------------#

#Duplicates keys
dict3 = {
    "name":"anu",
    "name":"fidha"
}
print(dict3)

#-------------------------------------------------------------------------------------#


#Accessing elements in a dictionary 

#1. using keys
student3 = {
    "name":"krishnendu",
    "age":23,
    "mark":97
}
print(student3["name"])
print(student3["age"])
print(student3["mark"])
#print(student[0]) ----> Not index based, ERROR
#print(student["number"]) ----> key not present in dictionary, ERROR

#---------------------------------------#

# 2. get()
student4 = {
    "name":"krishnendu",
    "age":23,
    "mark":97
}
print(student4.get("name"))
print(student4.get("age"))
print(student4.get("college"))
print(student4.get("number")) # if key doesnt exist ---> None
print(student4.get("number","Not available")) # We can set default value

#-------------------------------------------------------------------------------------#

#[] vs get()
    #[] gives error if key not present, not index based
    #get() returns None if key not present, set default value instead of none

#-------------------------------------------------------------------------------------#


#Adding an element

# 1. dicitonary["key"] = "value"
dictionary1 = {
    "name":"anu",
    "mark":89.7,
}
dictionary1["passed"] = True
print(dictionary1)

#Updating a value
dictionary1["mark"] = 75
print(dictionary1)

# if key already exists ----> updates the value
# if key doesnt exist ----> adds a new key-value pair
dictionary1["number"] = 75
print(dictionary1)

#-------------------------------------#

# 2. using update() - used to add or update one or more key value pairs
dictionary2 = {
    "name":"anu",
    "mark":89.7,
}
dictionary2.update({
    "roll_num":42,
    "mark1": 90
})
print(dictionary2)


#-------------------------------------------------------------------------------------#


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

#----------------------------------#

#2. popitem() - remove last inserted key-value pair
student.popitem()
print(student)

#----------------------------------#

#3. del - used to delete a specific key-value pair
del student["mark"]
print(student)

#----------------------------------#

# 4. clear - remove all elements from the dictionary
student.clear()
print(student)

#-------------------------------------------------------------------------------------#

#check existence of key
student = {
    "name":"parvathy",
    "age":20,
    "mark":98,
    "college":"SSET"
}
print("age" in student)