class_name = ['1a', '1b', '2a', '2b', '3a', '4a', '4b']
quantity_in_class = [21, 25, 19, 18, 17, 30, 23]

school = {key: value for key, value in zip(class_name, quantity_in_class)}

school['2a'] = 29   # зміна кількості учнів в однму класі
school['5a'] = 24   # додавання нового класу
school.pop('2b')    # видалення одного класу

quantity_in_school = sum(school.values())
print(f'Загальна кількість учнів у школі - {quantity_in_school}')

def reverse_dict(dict):
    return {value: key for key, value in dict.items()}

reverse_school = reverse_dict(school)
print(f'Початковий словник: {school} \n"Перевернутий" словник: {reverse_school}')
