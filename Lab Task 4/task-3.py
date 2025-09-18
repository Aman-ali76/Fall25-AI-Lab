def is_even(n):
    return n % 2 == 0

def card_validator(n):
    if not n.isdigit():
        return "Invalid input. Please enter a numeric string."
    
    digits = [int(i) for i in n]
    x = digits.pop()
    digits.reverse()
    for i,j in enumerate(digits):
        if is_even(i):
            digits[i] = j * 2
    
    for i,j in enumerate(digits):
        if j > 9:
            digits[i] = j - 9

    total_sum = sum(digits) + x
    if total_sum % 10 == 0:
        return "Your Card is Valid "
    else:
        return "Your Card is Invalid!"
    
number = input("Enter your card number: ")
print(card_validator(number))
    
    
    
