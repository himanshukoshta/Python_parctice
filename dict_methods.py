##  Add a new key-value pair (11, 121) to the dictionary created in Assignment 1
#  and then remove the key-value pair with key 1. Print the modified dictionary.
d1={i:i**2 for i in range(1,11)}
d1[11]=121
print(d1)
d1.pop(1)
print(d1)