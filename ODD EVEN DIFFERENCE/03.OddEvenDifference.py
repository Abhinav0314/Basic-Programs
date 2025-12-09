x = input('Enter the value of x: ')

odd_sum, even_sum = sum(int(digit) for position, digit in enumerate(x[::-1],1) if position & 1), sum(int(digit) for position, digit in enumerate(x[::-1]) if not position & 1)

print(odd_sum-even_sum)