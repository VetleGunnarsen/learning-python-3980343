# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values


# to access a member of a sequence type, use []
myList = [ 0, "one,", 2.3, True, 9, 10, 6 ]
print(len(myList))  # get the length of a sequence

# add a list to another list
print(myList[2])
print(myList[-2])
#myList[0] = 10
print(myList)

# use slices to get parts of a sequence
print(myList[2:6])
print(myList[2:6:1]) #skips every 1 item

# you can use slices to reverse a sequence
print(myList[-0])


# Tuples are like lists, but they are immutable
myTuple = ( 0, "one,", 2.3, True, 9, 10, 6 )
print(myTuple[0])

# Sets are also sequences, but they contain unique values
mySet = { 0, "one,", 0, True, 9, 10, 6 } #Will remove duplicates
print(mySet)
mySet2 = { 7, 8, 9 }



# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(mySet2)
print(0 in mySet)
print(0 in mySet2)