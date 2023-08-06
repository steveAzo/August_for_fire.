def is_tidy(number):
    number_in_list_form = list(str(number))
    for i in range(len(number_in_list_form) - 1):
        if number_in_list_form[i] > number_in_list_form[i + 1]:
            return False
    return True 
    
number = int(input("Enter a number to check:"))
print(is_tidy(number))
