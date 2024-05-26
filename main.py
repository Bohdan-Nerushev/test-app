from random import randint, shuffle
import csv
import pickle
from pprint import pprint

# Декоратор для виводу помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)

    return inner

# Архівує список
@input_error
def add__member__word(word_dict: list = [], FILENAME: str = "word.csv"):
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        columns = word_dict[0].keys()
        writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
        writer.writeheader()
        for row in word_dict:
            writer.writerow(row)
    return 'Дані збережено'

# Розархівовує список
@input_error
def open_member_word(FILENAME="word.csv"):
    with open(FILENAME, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        a = []
        for row in reader:
            a.append(row)
    return a
    print('=======')


# Додає слова в список
@input_error
def add_word(word_dict: list = []):
    new_word_d = input("Введіть нове слово німецькою: ").strip()
    new_word_uk = input("Введіть переклад слова українською: ").strip()
    word_dict.append({'d': new_word_d, 'uk': new_word_uk})
    return add__member__word(word_dict)
    print('=======')


# Оновлює слова у списку(укр.)
@input_error
def update_word_translet_uk(word_dict: list = []):
    alt_word_uk = input("Введіть старе слово українською: ").strip()
    new_word_uk = input("Введіть оновлене слово українською: ").strip()
    found = False
    for i in word_dict:
        if i.get('Ukrain') == alt_word_uk:
            i.update({'Ukrain': new_word_uk})
            found = True
            break
    if found:
        add__member__word(word_dict)  # Зберігаємо оновлений словник у файл
        return f'Переклад слова {alt_word_uk} оновлено на {new_word_uk}.'
    else:
        return f'Слово "{alt_word_uk}" не знайдено.'
    print('=======')


# Оновлює слова у списку(нім.)
@input_error
def update_word_translet_d(word_dict: list = []):

    alt_word_d = input("Введіть старе слово німецькою: ").strip()
    new_word_d = input("Введіть оновлене слово німецькою: ").strip()
    found = False
    for i in word_dict:
        if i.get('Deutsch') == alt_word_d:
            i.update({'Deutsch': new_word_d})
            found = True
            break
    if found:
        add__member__word(word_dict)  # Зберігаємо оновлений словник у файл
        return f'Переклад слова {alt_word_d} оновлено на {new_word_d}.'
    else:
        return f'Слово "{alt_word_d}" не знайдено.'
    print('=======')

# Видаляє слово
@input_error
def delet_word(word_dict: list = []):

    alt_word = input("Введіть  слово для видалення: ").strip()
    found = False
    for i in word_dict:
        if i.get('Deutsch') == alt_word or i.get('Ukrain') == alt_word:
            word_dict.pop(word_dict.index(i))

            found = True
            break

    if found:
        add__member__word(word_dict)  # Зберігаємо оновлений словник у файл
        return f'Слова {alt_word} видалено.'
    else:
        return f'Слово "{alt_word}" не знайдено.'
    print('=======')



# Генерує питання для тесту
@input_error
def frage(word_dict: list = []):
    random_wariant = []
    war_ant = []


# Генеруємо рандомні значення.(Варіантів відповіді)
    while len(random_wariant) < 4:
        num = randint(0, len(word_dict) - 1)
        if num not in random_wariant:
            random_wariant.append(num)
# Генеруємо рандомні значення. (Варіанти розташування відповідей)
    random_wariant_c = list(range(4))
    shuffle(random_wariant_c)

# Друкуємо питання
    print(word_dict[random_wariant[1]].get('Ukrain'))
    frag = word_dict[random_wariant[1]].get('Ukrain')
# Друкуємо варіанти відповіді
    print('=======')
    for i in range(4):
        c = random_wariant_c[i]
        print(word_dict[random_wariant[c]].get('Deutsch'), '\t', i)
        war_ant.append(word_dict[random_wariant[c]].get('Ukrain'))
    print('=======')

# Перевіряємо правильність відповіді
    b = int(input('Введіть відповідь (0, 1, 2, 3): '))
    if war_ant[b] == frag:  # Перевірка відповіді
        return '+=+ Правильно +=+'
    else:
        return '+=+ Неправильно +=+'
    print('=======')



def main():
    word_dict = open_member_word(FILENAME="word.csv")
    while True:

        print('+=======+=======+=======+=======+')
        print('Доступні команди: test, add_word, update_word_uk, update_word_d, show_all_word, delet_word, close ')
        print('=======')
        a = input('Введіть kоманду: ').strip()
        print('=======')

        if a == 'close': # Завершує виконання програми
            print('До побачення :)')
            break

        elif a == 'test': # Запускає тест
            print(frage(word_dict))

        elif a == 'add_word': # Додає слово в список
            print(add_word(word_dict))

        elif a == 'update_word_uk': # Оновлює значення перекладу
            print(update_word_translet_uk(word_dict))

        elif a == 'update_word_d': # Оновлює значення слова
            print(update_word_translet_d(word_dict))

        elif a == 'delet_word': # Видаляє слово
            print(delet_word(word_dict))

        elif a == 'show_all_word': # Виведе всі слова і переклади
            pprint(word_dict)

        else: # Команду не знайдено
            print('Команду не знайдено\n')


if __name__ == '__main__':
    main()





