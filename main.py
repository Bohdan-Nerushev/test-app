from random import randint, shuffle
import csv
import pickle
from pprint import pprint


def add__member__word(word_dict: list = [], FILENAME: str = "word.csv"):
    try:
        with open(FILENAME, "w", encoding="utf-8", newline="") as f:
            columns = word_dict[0].keys()
            writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
            writer.writeheader()
            for row in word_dict:
                writer.writerow(row)
        return 'Дані збережено'
    except Exception as e:
        print('=======')
        return e


def open_member_word(FILENAME="word.csv"):
    try:
        with open(FILENAME, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            a = []
            for row in reader:
                a.append(row)
        return a
    except Exception as e:
        print('=======')
        return e


# Додає слова в список
def add_word(word_dict: list = []):
    try:
        new_word_d = input("Введіть нове слово німецькою: ").strip()
        new_word_uk = input("Введіть переклад слова українською: ").strip()
        word_dict.append({'d': new_word_d, 'uk': new_word_uk})
        return add__member__word(word_dict)
    except Exception as e:
        print('=======')
        return e


# Оновлює слова у списку(укр.)
def update_word_translet_uk(word_dict: list = []):
    try:
        alt_word_uk = input("Введіть старе слово українською: ").strip()
        new_word_uk = input("Введіть оновлене слово українською: ").strip()
        found = False
        for i in word_dict:
            if i.get('uk') == alt_word_uk:
                i.update({'uk': new_word_uk})
                found = True
                break
        if found:
            add__member__word(word_dict)  # Зберігаємо оновлений словник у файл
            return f'Переклад слова {alt_word_uk} оновлено на {new_word_uk}.'
        else:
            return f'Слово "{alt_word_uk}" не знайдено.'
    except Exception as e:
        print('=======')
        return e


# Оновлює слова у списку(нім.)
def update_word_translet_d(word_dict: list = []):
    try:
        alt_word_d = input("Введіть старе слово німецькою: ").strip()
        new_word_d = input("Введіть оновлене слово німецькою: ").strip()
        found = False
        for i in word_dict:
            if i.get('d') == alt_word_d:
                i.update({'d': new_word_d})
                found = True
                break
        if found:
            add__member__word(word_dict)  # Зберігаємо оновлений словник у файл
            return f'Переклад слова {alt_word_d} оновлено на {new_word_d}.'
        else:
            return f'Слово "{alt_word_d}" не знайдено.'
    except Exception as e:
        print('=======')
        return e


# Видаляє слово
def delet_word(word_dict: list = []):
    try:
        alt_word = input("Введіть  слово для видалення: ").strip()
        found = False
        for i in word_dict:
            if i.get('d') == alt_word or i.get('uk') == alt_word:
                word_dict.pop(word_dict.index(i))

                found = True
                break

        if found:
            add__member__word(word_dict)  # Зберігаємо оновлений словник у файл
            return f'Слова {alt_word} видалено.'
        else:
            return f'Слово "{alt_word}" не знайдено.'
    except Exception as e:
        print('=======')
        return e


# генерує питання для тесту
def frage(word_dict: list = []):
    random_wariant = []
    war_ant = []
    try:

        # Генеруємо рандомні значення.(Варіантів відповіді)
        while len(random_wariant) < 4:
            num = randint(0, len(word_dict) - 1)
            if num not in random_wariant:
                random_wariant.append(num)
        # Генеруємо рандомні значення. (Варіанти розташування відповідей)
        random_wariant_c = list(range(4))
        shuffle(random_wariant_c)

        # Друкуємо питання
        print(word_dict[random_wariant[1]].get('uk'))
        frag = word_dict[random_wariant[1]].get('uk')
        # Друкуємо варіанти відповіді
        print('=======')
        for i in range(4):
            c = random_wariant_c[i]
            print(word_dict[random_wariant[c]].get('d'), '\t', i)
            war_ant.append(word_dict[random_wariant[c]].get('uk'))
        print('=======')

        # Перевіряємо правильність відповіді
        b = int(input('Введіть відповідь (0, 1, 2, 3): '))
        if war_ant[b] == frag:  # Перевірка відповіді
            return '   Правильно\n'
        else:
            return '   Неправильно\n'
    except Exception as e:
        print('=======')
        return e


def main():
    word_dict = open_member_word(FILENAME="word.csv")
    while True:

        print('+=======+=======+=======+=======+')
        print('Доступні команди: test, add_word, update_word_uk, update_word_d, show_all_word, delet_word, close ')
        print('=======')
        a = input('Введіть kоманду: ').strip()
        print('=======')

        if a == 'close':
            print('До побачення :)')
            break

        elif a == 'test':
            print(frage(word_dict))

        elif a == 'add_word':
            print(add_word(word_dict))

        elif a == 'update_word_uk':
            print(update_word_translet_uk(word_dict))

        elif a == 'update_word_d':
            print(update_word_translet_d(word_dict))

        elif a == 'delet_word':
            print(delet_word(word_dict))

        elif a == 'show_all_word':
            pprint(word_dict)

        else:
            print('Команду не знайдено\n')


if __name__ == '__main__':
    main()





