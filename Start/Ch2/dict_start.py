# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
myDict = {
    "username": "slayer123",
    "password": "mypassword",
    "controlnumber": 42,
    2.6 : [1, 2, 3]
}

#Dictionaries are accessed by key
print(myDict["username"])
print(myDict[2.6])


# you can also set dictionary data by creating a new key
myDict["email"] = "user@example.com"
print(myDict)
# Trying to access a nonexistent key will produce an error
# print(myDict["username1"])

# To avoid this, you can use the "in" operator to see if a key exists
print("username" in myDict) 
print("username1" in myDict)

# You can retrieve all of the keys and values from a dictionary


# You can also iterate over all the items in a dictionary
