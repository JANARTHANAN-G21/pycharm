#initialize an empty list
my_list = []

#append an element to the list
my_list.append(11)

#remove an element from the list
if 11 in my_list:
    my_list.remove(11)

#generate a list of squares of numbers from 1 to 10 using list comprehension
squares_list = [x**2 for x in range(1, 11)]

#sort the list in ascending order
squares_list.sort()

#reverse the list
squares_list.reverse()
#modified list
print("Modified List:", squares_list)
