# Assignment
# Programmer: Rashaun Forrest
# Date: 06/02/2016
# Purpose: Get desired results by creating a class that produces desired output


from MaxSizeList import MaxSizeList


a = MaxSizeList(3)
b = MaxSizeList(1)

# Add these 4 and pop "hey"
a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

# Add these 4 and pop the first 3
b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

# Use getter method to get the list
print(a.get_list())
print(b.get_list())

# Desired output
# ['hi', "let's", 'go']
# ['go']
