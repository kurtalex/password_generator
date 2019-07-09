import random
import string


def pass_generator(char_count=8):
    nums = tuple(string.digits)
    lower_words = tuple(string.ascii_lowercase)
    upper_words = tuple(string.ascii_uppercase)
    lower_words_and_nums = tuple(string.ascii_lowercase + string.digits)
    upper_words_and_nums = tuple(string.ascii_uppercase + string.digits)
    all_words_and_nums = tuple(string.ascii_letters + string.digits)
    all_symbols = tuple(string.printable)
    passw = []
    if choice in range(1, 8):
        if choice == 1:
            for i in range(char_count):
                passw.append(random.choice(nums))
        elif choice == 2:
            for i in range(char_count):
                passw.append(random.choice(lower_words))
        elif choice == 3:
            for i in range(char_count):
                passw.append(random.choice(upper_words))
        elif choice == 4:
            for i in range(char_count):
                passw.append(random.choice(lower_words_and_nums))
        elif choice == 5:
            for i in range(char_count):
                passw.append(random.choice(upper_words_and_nums))
        elif choice == 6:
            for i in range(char_count):
                passw.append(random.choice(all_words_and_nums))
        elif choice == 7:
            for i in range(char_count):
                passw.append(random.choice(all_symbols))
    else:
        print("Некорректный ввод!!!")
    return "".join(passw)


n = int(input("Введите размер пароля: "))
print("""
1. Пароль состоящий из цифр
2. Пароль состоящий из букв(нижний регистр)
3. Пароль состоящий из букв(верхний регистр)
4. Пароль состоящий из цифр+букв(нижний регистр)
5. Пароль состоящий из цифр+букв(верхний регистр)
6. Пароль состоящий из цифр+букв(верхгий+нижний регистр)
7. Пароль состоящий из любых символов
""")
choice = int(input("Выберите сложность пароля: "))
print(pass_generator(n))
input("Нажмите Enter для завершения программы.")
