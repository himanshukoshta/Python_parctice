## Create a new set containing only the even numbers from the set created 
# in Assignment 1 using a set comprehension. Print the new set.
set1={1,2,3,4,5,6,7,8,9,10}
new_set={i for i in set1 if i%2==0}
print(new_set)
