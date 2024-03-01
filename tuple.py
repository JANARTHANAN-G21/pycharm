# Accessing elements of a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Sliced tuple:", my_tuple[2:5])

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# List of tuples
list_of_tuples = [(1, 5), (2, 3), (3, 8), (4, 1), (5, 2)]

# Sorting based on the second element of each tuple
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

print("sorted list:",sorted_list)