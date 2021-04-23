num = int(input("Give me a number! "))
check = int(input("Give me another number! "))

if num % check: 
    print(f"{num} is not divisible by {check}!")
    
else:
    print(f"{num} is divisible by {check}!")