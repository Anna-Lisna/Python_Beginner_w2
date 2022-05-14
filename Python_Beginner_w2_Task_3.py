def print_two_sentence():
    sentences = []
    while len(sentences) < 2:
        sentence = input("Enter sentence ")
        if sentence:
            sentences.append(sentence)

    return ' '.join(sentences)

#print(print_two_sentence())


def validation(num):
    new_num = num.strip().replace('-', '')
    return new_num.isdigit()


def multiply_input_number():
    number = '1'
    multiply = 1
    counter = 0   # використала для спрощення перевірки якщо користувач одразу введе 0
    while number != '0':
        if validation(number):
            multiply *= int(number)
            counter += 1
        number = input("Enter number ")

    return 0 if counter == 1 else multiply

print(f'Result of multiple of entered numbers: {multiply_input_number()}')
