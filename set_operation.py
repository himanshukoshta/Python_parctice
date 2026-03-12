## Create two sets: one with the first 5 positive integers and another with the first 5 even integers.
#  Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
set1={1,2,3,4,5}
set2={2,4,6,8,10}

#union
unionn=set1.union(set2)
print(unionn)

#intersection
intersection_set=set1.intersection(set2)
print(intersection_set)

# difference
diff_set=set1.difference(set2)
print(diff_set)

# symmetric difference
sym_diff=set1.symmetric_difference(set2)
print(sym_diff)