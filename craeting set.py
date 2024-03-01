#creating a set

my_set = {1,2,3,4,5}
print(my_set)


#Adding elements to a set

my_set.add(6)
print(my_set)

#Removing an elements from a set

my_set.remove(3)
print(my_set)

#set is used to performed mathematical operations union.
#print(intersection and difference)they are also useful for eleminting duplicatefrom the list.lambda


#set operation

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

print(1 in set1)
print(9 in set1)

# in sets or python unorder collection so they dont support index slicing like
#sequence such as in list or string therefore there isnt direct method to reverse the
#set however to reverse the elements  of a set you can convert the set to list
#reverse the list add then convert back the set to the list

original_set = {1,2,3,4,5}
print("original_set:",original_set)

#convert set to list, reverse the list and convert it back to set

original_set = {1,2,3,4,5}
reversed_set = set(reversed(list(original_set)))
print("reversed set:",reversed_set)

