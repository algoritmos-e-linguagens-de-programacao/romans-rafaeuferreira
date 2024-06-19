def roman_to_int(roman):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    i = 0
    while i < len(roman):
        current_value = roman_map[roman[i]]
        if i + 1 < len(roman):
            next_value = roman_map[roman[i + 1]]
            if current_value >= next_value:
                result += current_value
            else:
                result += next_value - current_value
                i += 1  
        else:
            result += current_value
        i += 1
    return result

def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
    return roman_num

