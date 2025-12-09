from math import sqrt
def main():
    print('Please enter the sides of the Triangle:')
    try:
        a = float(input('Side 1: '))
        b = float(input('Side 2: '))
        c = float(input('Side 3: '))
        if a + b <= c or a + c <= b or b + c <= a:
            print('The given sides do not form a Triangle.')
            return
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print(f'The area of the Triangle is {area:.2f}')
    except ValueError:
        print('Please enter the valid numerical values.')
main()