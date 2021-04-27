# Exercise 1 + stretch goal c

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Give me a number! "))

result = [x for x in my_list if x < num]

print(result)