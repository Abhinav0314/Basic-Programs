chocolates,boxes = int(input('Please enter the no. of chocolates.')),0
if 0<=chocolates<=300:
    boxes = chocolates//12
    if chocolates%12!=0:
        boxes += 1
else:
    print('Invalid input for chocolates.')
print(f'The number of boxes needed are :{chocolates}')