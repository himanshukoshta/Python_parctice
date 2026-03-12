## Create a set with the first 5 positive integers. Convert it to a list, append the number 6,
#  and convert it back to a set. Print the resulting set.
set1={1,2,3,4,5}
lst=list(set1)
lst.append(6)
sr=set(lst)
print(sr)