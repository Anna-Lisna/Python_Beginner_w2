def positive():
    print("Positive")


def negative():
    print("Negative")


def validation(num):
    new_num = num.strip().replace('-', '')
    return new_num.isdigit()


def test():
    number = input("Enter a number ")
    while not validation(number):
        number = input("You entered not a number. Please, enter a number! ")
    if int(number) >= 0:
        positive()
    else:
        negative()

test()
#Не маєзначення фукції positive() і negative() створені до чи після визначення функції test().
# Головне, щоб всі фукції були визначені перед викликом функції test(), адже самк під час виклику відбувається пошук всіх змінних.
