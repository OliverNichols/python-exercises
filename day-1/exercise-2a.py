# Exercise 2 + stretch goal a

num = int(input("Give me a number! "))

if not num % 4:
    print(f"{num} is divisible by 4!")

elif not num % 2: 
    print(f"{num} is an even number!")
    
else:
    print(f"{num} is an odd number!")
