apples = int(input('Enter the number of apples.'))
fullbox = apples // 10
if fullbox % 10 != 0:
    fullbox = fullbox + 1
print(f'Total no. of minimum box required is {fullbox}.')