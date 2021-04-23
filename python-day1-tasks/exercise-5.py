my_list = [5, 10, 15, 20, -25, -30]

# only first and last elements
first_task = [my_list[0], my_list[-1]]
print(first_task)

# duplicate all elements
second_task = [x for dupe in zip(my_list, my_list) for x in dupe]
print(second_task)

# reverse order of elements
third_task = list(reversed(my_list))
print(third_task)

# sorted in descending order
fourth_task = sorted(my_list, reverse=True)
print(fourth_task)