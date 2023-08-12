def solution(roman):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    prev_value = 0

    for symbol in roman[::-1]:  # Process the symbols in reverse order
        value = values[symbol]
        
        if value >= prev_value:
            num += value
        else:
            num -= value

        prev_value = value
    
    return num