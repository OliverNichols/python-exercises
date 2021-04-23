my_string = "ABCdeFhIjklmNOP"

index = (len(my_string)-3) // 2

print( 
    my_string[:index].lower() + 
    my_string[index:index+3].upper() + # we can spread strings over multiple lines using the + operator
    my_string[index+3:].lower()
)