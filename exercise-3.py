my_string = "ABCdeFhIjklmNOP"

index = (len(my_string)-3) // 2

if len(my_string) > 7 and len(my_string)%2:
    print(my_string[:index].lower() + my_string[index:index+3].upper() + my_string[index+3:].lower())

else:
    pass