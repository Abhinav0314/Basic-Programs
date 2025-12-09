number = int(input('Enter a number:\n')[::-1])

digits = []

while number > 0:  
    digits.append((number % 10) ** 2)
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


