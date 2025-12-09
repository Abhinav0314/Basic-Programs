n = int(input('Enter the no. of days.'))
sales = list(map(int, input('Enter tha sales with spaces.').split()))
average = sum(sales)/n
average_days = 0
for sale in sales:
    if sale > average:
        average_days += 1
print(f'The no. of days having average sales are {average_days}.')