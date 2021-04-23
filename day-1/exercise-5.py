# Exercise 5

my_list = [5, 10, 15, 20, -25, -30]

# 5.1. only first and last elements
first_task = [my_list[0], my_list[-1]]
print(first_task)

# 5.2. duplicate all elements
second_task = [x for dupe in zip(my_list, my_list) for x in dupe]
print(second_task)

# 5.3. reverse order of elements
third_task = list(reversed(my_list))
print(third_task)

# 5.4. sorted in descending order
fourth_task = sorted(my_list, reverse=True)
print(fourth_task)