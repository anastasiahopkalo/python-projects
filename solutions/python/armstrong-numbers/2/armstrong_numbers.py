def is_armstrong_number(number):
    number_str = str(number)
    length = len(number_str)
    result = 0
    for i in range (0, length):
        result += int(number_str[i]) ** length
    if result == number :
        return True
    return False
