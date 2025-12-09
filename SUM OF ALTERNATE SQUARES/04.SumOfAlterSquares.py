number = int(input('Enter a number:\n'))

digits = []

while number > 0:  
    digits.insert(0,(number % 10) ** 2)
    number = number // 10

position = 1

sum = 0

for digit in digits:
    if position & 1:
        sum = sum + digit

    else:
        sum = sum - digit

    position += 1

print(sum)