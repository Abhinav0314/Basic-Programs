num1,num2,factor1,factor2 = int(input('Please enter first number.')), int(input('Please enter second number.')),0,0
for i in range(1,num1):
    if num1 % i == 0:
        factor1 = factor1 + i
x = factor1 / num1
for i in range(1,num2):
    if num2 % i == 0:
        factor2 = factor2 + i
y = factor2 / num2
if x == y:
    print(f'{num1} and {num2} are Fiendly numbers.')
else:
    print(f'{num1} and {num2} are not Fiendly numbers.')