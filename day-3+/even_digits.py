def even_digits(a:int, b:int) -> str:
    if a > b: b, a = a, b # works if a > b
    
    output = []
    for n in range(a, b+1):
        for digit in str(n):
            if digit == '-': continue # works for negative numbers too
            elif int(digit)%2: break

        else: output.append(str(n))
    return ','.join(output)