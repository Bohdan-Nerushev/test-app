from random import randint, shuffle
import csv
import pickle

def add__member__word(word_dict:list = [], FILENAME:str = "word.csv"):
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        columns = word_dict[0].keys()
        writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
        writer.writeheader()
        for row in word_dict:
            writer.writerow(row)
    return 'Дані збережено'

def open_member_word(FILENAME = "word.csv"):
    with open(FILENAME, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        a = []
        for row in reader:
            a.append(row)
    return a

def frage(word_dict:list):
    random_wariant = []
    war_ant = []
    # Генеруємо рандомні значення
    while len(random_wariant) < 4:
        num = randint(0, len(word_dict) - 1)
        if num not in random_wariant:
            random_wariant.append(num)
    # Генеруємо рандомні значення
    random_wariant_c = list(range(4))
    shuffle(random_wariant_c)

    print(word_dict[random_wariant[1]].get('uk'))
    frag = word_dict[random_wariant[1]].get('uk')

    print('=======')
    for i in range(4):
        c = random_wariant_c[i]
        print(word_dict[random_wariant[c]].get('d'), '\t', i)
        war_ant.append(word_dict[random_wariant[c]].get('uk'))
    print('=======')

    try:
        b = int(input('Введіть відповідь (0, 1, 2, 3): '))
        if war_ant[b] == frag:  # Перевірка відповіді
            return 'Правильно\n+=======+'
        else:
            return 'Неправильно\n+=======+'
    except Exception as e:
        return str(e)

def main():
    word_dict = open_member_word(FILENAME="word.csv")
    while True:
        print('Доступні команди: ')
        a = input('Введіть kоманду: ').strip()
        if a == 'close':
            print('До побачення')
            break
        elif a == 'test':
            print(frage(word_dict))
        elif a == 'add_word':
            # Виклик функції для додавання слів не був визначений, тому додано це як виклик функції
            new_word_d = input("Введіть нове слово німецькою: ").strip()
            new_word_uk = input("Введіть переклад слова українською: ").strip()
            word_dict.append({'d': new_word_d, 'uk': new_word_uk})
            print(add__member__word(word_dict))
        else:
            print('Команду не знайдено')

if __name__ == '__main__':
    main()





