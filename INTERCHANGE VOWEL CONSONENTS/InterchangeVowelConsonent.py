def main():
    vowels = 'aeiouAEIOU'
    string = input('Please enter a string.')
    vowel_list = [ch for ch in string if ch in vowels]
    
    if not vowel_list:
        return 'No vowels found in the string.'
    
    result = []
    vowel_index = 0

    for ch in string:
        if ch.isalpha() and ch not in vowels:
            result.append(vowel_list[vowel_index])
            vowel_index = (vowel_index + 1) % len(vowel_list)
        else:
            result.append(ch)
    return ''.join(result)
print('The string after changes is:',main())