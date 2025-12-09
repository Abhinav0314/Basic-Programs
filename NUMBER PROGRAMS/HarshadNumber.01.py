number = input('Please enter a number.')
sum = 0
for digit in number:
    sum = sum + int(digit)
    if int(number) % sum == 0:
        print(f'{number} is a Harshad number.')
        break