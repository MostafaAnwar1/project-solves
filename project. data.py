
start = int(input('Enter Start: '))
end = int(input('Enter End: '))

def divide_numbers(start, end):
    even_numbers = []
    odd_numbers = []
    
    for number in range(start, end + 1): 
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)


divide_numbers(start, end)
