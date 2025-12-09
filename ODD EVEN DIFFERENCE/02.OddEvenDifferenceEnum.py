x = input('enter the value of x: ')

odd_sum,even_sum = [0,0]

for position,digit in enumerate(x[::-1],1):
    if position & 1:
        odd_sum = odd_sum + int(digit)
    else:
        even_sum = even_sum + int(digit)

result = odd_sum - even_sum

print(result)