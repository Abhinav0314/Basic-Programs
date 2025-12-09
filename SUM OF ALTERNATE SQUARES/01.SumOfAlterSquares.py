number = int(input('Enter a number:\n'))

digits = []

while number > 0:  
    digits.append((number % 10) ** 2)
    number = number // 10

temp = []

for index in range(len(digits)-1,-1,-1):
    temp.append(digits[index])

position = 1

sum = 0

for digit in temp:
    if position & 1:
        sum = sum + digit

    else:
        sum = sum - digit

    position += 1

print(sum)