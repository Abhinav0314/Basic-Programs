sides = input('Please enter the sides.').split()
if len(sides) > 3:
    'bakwas Fellows'
else:
    sides = [int(side) for side in sides]
    sides.sort()
    if 0<sides[0]<=sides[1]<=sides[-1] and sides[0]+sides[1]>sides[-1]:
        s= sum(sides)/2
        area = (s*(s-sides[0])*(s-sides[1])*(s-sides[-1])** 0.5)
        print(f'The area of the triangle is {area}')
    else:
        print('Invalid input for triangle sides.')