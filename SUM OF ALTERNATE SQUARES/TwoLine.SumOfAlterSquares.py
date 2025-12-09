n = [int(digit)**2 for digit in input('Enter the number:\n')]

print(sum(n[::2])-sum(n[1::2]))

