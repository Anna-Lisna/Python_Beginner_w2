# Part_1
def get_unicode_symbol():
    number = input("Enter Unicode number ")
    while number != '0':
        if number.isdigit() and int(number) <= 1114111:
            print(f'You entered {number} - it is symbol in Unicode {chr(int(number))}')
        number = input("Enter Unicode number ")

get_unicode_symbol()


# Part_2
def write_ten_symbol():
    string = input("Enter sentence ")
    string_length = len(string)
    if string_length > 10:
        print("Warning! String length is more than 10 symbol")
    else:
        print(string.ljust(10, '*'))

write_ten_symbol()


# Part_3
def validation(float_number):
    clear_number = float_number.strip().replace('-', '')
    if clear_number.isdigit():
        result = True
    else:
        float_part = clear_number.split('.')
        result = float_part[0].isdigit() and float_part[1].isdigit()
    return result


def get_float_numbers():
    float_numbers = []
    while len(float_numbers) < 6:
        float_number = input("Enter float number ")
        if validation(float_number):
            float_numbers.append(float(float_number))

    get_min_and_max(float_numbers)


def get_min_and_max(float_numbers):
    min = float_numbers[0]
    max = float_numbers[0]
    for i in float_numbers:
        if i < min:
            min = i
        if i > max:
            max = i
    print(f'Max: {max:.2f}, min: {min:.2f}')

get_float_numbers()
