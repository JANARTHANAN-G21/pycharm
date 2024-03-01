
fruit = {}

fruit['apple'] = 5
fruit['banana'] = 3
fruit['orange'] = 7

print("Number of apples:", fruit['apple'])
print("Number of oranges:", fruit['orange'])

# Removing a key
del fruit['banana']
print("Dictionary after removing 'banana':", fruit)

#Dictionary Comprehension:
#Write a program that generates a dictionary where
# keys are numbers from 1 to 5, and values are the squares of the keys.

square_dict = {num: num**2 for num in range(1, 6)}
print(square_dict)

#Dictionary Sorting:
#Write a program to sort a dictionary
# by its values in ascending order.

# Dictionary to be sorted
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 1, 'kiwi': 4}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)

#Write a program that merges two dictionaries into one.

my_dict = {'apple': 5, 'banana': 3, 'orange': 7,}
my_dict2 = {'grape': 1, 'kiwi': 4}

merged_dict = {**my_dict,**my_dict2}
print("merged dictionary:",merged_dict)