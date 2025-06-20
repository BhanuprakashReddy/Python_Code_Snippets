# Basic string operations in Python

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)

# Repetition
repeat = str1 * 3
print("Repetition:", repeat)

# Length
length = len(str1)
print("Length:", length)

# Slicing
slice_str = str1[1:4]
print("Slicing:", slice_str)

# Upper and lower case
print("Upper:", str1.upper())
print("Lower:", str2.lower())

# Replace
replaced = str2.replace("World", "Python")
print("Replace:", replaced)

# Split
split_str = result.split(" ")
print("Split:", split_str)

# Join
joined = "-".join(split_str)
print("Join:", joined)

# Find
index = result.find("World")
print("Find:", index)

# Strip
whitespace_str = "   Hello World   "
print("Strip:", whitespace_str.strip())