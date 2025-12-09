number = int(input("Enter a number: "))
odd_sum = 0  
even_sum = 0  
position = 1  

while number > 0:
    digit = number % 10  
        
    if position % 2 == 1:  
        odd_sum += digit
    else:  
        even_sum += digit
        
    number //= 10  
    position += 1  

    result = odd_sum - even_sum

print("The result is:", result)
