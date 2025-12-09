student = int(input('Please enter the no. of students'))
if student < 1 or student > 30:
    print('You have entered the incorrect number of students.')
else:
    heights = []
    for i in range(student):
        height = int(input('Please enter the height of students.'))
        if height < 1 or height > 200:
            print('You have incorrect height of students.')
            break
        heights.append(height)
    else:
        avg_height = sum(heights) / student
        print(f'Average height of students is {avg_height}.')
        count_tall = 0
        for a in heights:
            if a > avg_height:
                count_tall += 1
    print(f'The no. of students taller thean avearge height are :{count_tall}')