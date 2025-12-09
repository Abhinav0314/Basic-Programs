number = int(input('Enter a number:\n'))
position = 1
sum = 0
for position,digit in enumerate(number,1):
    sqr = int(digit)**2

    if position & 1:
        sum = sum + sqr
    
    else:
        sum = sum - sqr
    
    position += 1

print(sum)