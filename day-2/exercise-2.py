# Exercise 2

for i in range(1, 51):
    
    result = ''

    if not i%3:
        result += 'Fizz'

    if not i%5:
        result += 'Buzz'

    print(result or i) # if there is a result, then use it, else use the number i