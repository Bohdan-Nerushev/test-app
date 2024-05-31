from random import randint, shuffle
import csv
from pprint import pprint

# Decorator to handle and display errors
# #Dekorator zur Behandlung und Anzeige von Fehlern
# Декоратор для обробки та відображення помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return inner

# Save the word list to a CSV file
# #Speichern Sie die Wortliste in einer CSV-Datei
# #Збережіть список слів у файл CSV
@input_error
def add__member__word(word_dict: list = [], FILENAME: str = "word.csv"):
    with open(FILENAME, "w", encoding="utf-8", newline="") as f:
        columns = word_dict[0].keys()
        writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
        writer.writeheader()
        for row in word_dict:
            writer.writerow(row)
    return 'Data saved' #Daten gespeichert #Дані збережено

# Load the word list from a CSV file
# #Laden Sie die Wortliste aus einer CSV-Datei
# #Завантажте список слів із файлу CSV
@input_error
def open_member_word(FILENAME="word.csv"):
    with open(FILENAME, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        a = []
        for row in reader:
            a.append(row)
    return a

# Add a new word to the list
# Fügen Sie der Liste ein neues Wort hinzu
# Додайте нове слово до списку
@input_error
def add_word(word_dict: list = []):
    new_word_d = input("Enter the new word in German: ").strip() #Geben Sie das neue Wort auf Deutsch ein #Введіть нове слово німецькою
    new_word_uk = input("Enter the translation of the word in Ukrainian: ").strip() #Geben Sie die Übersetzung des Wortes auf Ukrainisch ein #Введіть переклад слова українською
    word_dict.append({'Deutsch': new_word_d, 'Ukrain': new_word_uk})
    return add__member__word(word_dict)

# Update the Ukrainian translation of a word in the list
# #Aktualisieren Sie die ukrainische Übersetzung eines Wortes in der Liste
# #Оновіть український переклад слова у списку
@input_error
def update_word_translet_uk(word_dict: list = []):
    alt_word_uk = input("Enter the old word in Ukrainian: ").strip() #Geben Sie das alte Wort auf Ukrainisch ein #Введіть старе слово українською
    found = False
    for i in word_dict:
        if i.get('Ukrain') == alt_word_uk:
            new_word_uk = input("Enter the updated word in Ukrainian: ").strip() #Geben Sie das aktualisierte Wort auf Ukrainisch ein #Введіть оновлене слово українською
            i.update({'Ukrain': new_word_uk})
            found = True
            break
    if found:
        add__member__word(word_dict)  # Save the updated list to file #Speichern Sie die aktualisierte Liste in der Datei #Збережіть оновлений список у файл
        return f'The translation of the word {alt_word_uk} has been updated to {new_word_uk}.' #Die Übersetzung des Wortes {alt_word_uk} wurde auf {new_word_uk} aktualisiert. #Переклад слова {alt_word_uk} було оновлено на {new_word_uk}.
    else:
        return f'The word "{alt_word_uk}" was not found.' #Das Wort "{alt_word_uk}" wurde nicht gefunden. #Слово "{alt_word_uk}" не знайдено.

# Update the German word in the list
# #Aktualisieren Sie das deutsche Wort in der Liste
# #Оновіть німецьке слово у списку
@input_error
def update_word_translet_d(word_dict: list = []):
    alt_word_d = input("Enter the old word in German: ").strip() #Geben Sie das alte Wort auf Deutsch ein #Введіть старе слово німецькою
    found = False
    for i in word_dict:
        if i.get('Deutsch') == alt_word_d:
            new_word_d = input("Enter the updated word in German: ").strip() #Geben Sie das aktualisierte Wort auf Deutsch ein #Введіть оновлене слово німецькою
            i.update({'Deutsch': new_word_d})
            found = True
            break
    if found:
        add__member__word(word_dict)  # Save the updated list to file #Speichern Sie die aktualisierte Liste in der Datei #Збережіть оновлений список у файл
        return f'The translation of the word {alt_word_d} has been updated to {new_word_d}.' #Die Übersetzung des Wortes {alt_word_d} wurde auf {new_word_d} aktualisiert. #Переклад слова {alt_word_d} було оновлено на {new_word_d}.
    else:
        return f'The word "{alt_word_d}" was not found.' #Das Wort "{alt_word_d}" wurde nicht gefunden. #Слово "{alt_word_d}" не знайдено.

# Delete a word from the list
# Löschen Sie ein Wort aus der Liste
# Видаліть слово зі списку
@input_error
def delet_word(word_dict: list = []):
    alt_word = input("Enter the word to delete: ").strip() #Geben Sie das zu löschende Wort ein #Введіть слово для видалення
    found = False
    for i in word_dict:
        if i.get('Deutsch') == alt_word or i.get('Ukrain') == alt_word:
            word_dict.pop(word_dict.index(i))
            found = True
            break
    if found:
        add__member__word(word_dict)  # Save the updated list to file #Speichern Sie die aktualisierte Liste in der Datei #Збережіть оновлений список у файл
        return f'The word {alt_word} has been deleted.' #Das Wort {alt_word} wurde gelöscht. #Слово {alt_word} було видалено.
    else:
        return f'The word "{alt_word}" was not found.' #Das Wort "{alt_word}" wurde nicht gefunden. #Слово "{alt_word}" не знайдено.

# Generate a question for the test
# Erzeugen Sie eine Frage für den Test
# Генеруйте запитання для тесту
@input_error
def frage(word_dict: list = []):
    random_variant = []
    war_ant = []

    # Generate random indices for answer options
    # Erzeugen Sie zufällige Indizes für Antwortoptionen
    # Генеруйте випадкові індекси для варіантів відповідей
    while len(random_variant) < 4:
        num = randint(0, len(word_dict) - 1)
        if num not in random_variant:
            random_variant.append(num)

    # Shuffle the indices to randomize answer positions
    # Mischen Sie die Indizes, um die Antwortpositionen zu randomisieren
    # Перемішайте індекси, щоб рандомізувати позиції відповідей
    random_variant_c = list(range(4))
    shuffle(random_variant_c)

    # Print the question in Ukrainian
    # Drucken Sie die Frage auf Ukrainisch
    # Друкуйте запитання українською
    print(word_dict[random_variant[1]].get('Ukrain'))
    frag = word_dict[random_variant[1]].get('Ukrain')

    # Print the answer options in German
    # Drucken Sie die Antwortoptionen auf Deutsch
    # Друкуйте варіанти відповідей німецькою
    for i in range(4):
        c = random_variant_c[i]
        print(word_dict[random_variant[c]].get('Deutsch'), '\t', i)
        war_ant.append(word_dict[random_variant[c]].get('Ukrain'))

    # Check the answer
    # Überprüfen Sie die Antwort
    # Перевірте відповідь
    b = int(input('Enter the answer (0, 1, 2, 3): '))
    if war_ant[b] == frag:  # Validate the answer #Antwort validieren #Валідируйте відповідь
        return '+=+ Correct +=+' 
    else:
        return '+=+ Incorrect +=+'

# Print a separator line
# Drucken Sie eine Trennlinie
# Друкуйте розділювальну лінію
def prob():
    print('=======')

def main():
    word_dict = open_member_word(FILENAME="word.csv")
    while True:
        print('+=======+=======+=======+=======+')
        print('Available commands: test, add_word, update_word_uk, update_word_d, show_all_word, delet_word, close ') #Verfügbare Befehle: test, add_word, update_word_uk, update_word_d, show_all_word, delet_word, close #Доступні команди: test, add_word, update_word_uk, update_word_d, show_all_word, delet_word, close
        prob()
        a = input('Enter a command: ').strip() #Geben Sie einen Befehl ein #Введіть команду
        prob()
        if a == 'close' or a == 'exit' or a == 'stop': # Exit the program #Beenden Sie das Programm #Вийти з програми
            print('Goodbye :)') #Auf Wiedersehen :) #До побачення :)
            break
        elif a == 'test': # Start the test #Starten Sie den Test #Почати тест
            print(frage(word_dict))
        elif a == 'add_word': # Add a new word #Ein neues Wort hinzufügen #Додати нове слово
            print(add_word(word_dict))
        elif a == 'update_word_uk': # Update the Ukrainian translation #Die ukrainische Übersetzung aktualisieren #Оновити український переклад
            print(update_word_translet_uk(word_dict))
        elif a == 'update_word_d': # Update the German word #Das deutsche Wort aktualisieren #Оновити німецьке слово
            print(update_word_translet_d(word_dict))
        elif a == 'delet_word': # Delete a word #Ein Wort löschen #Видалити слово
            print(delet_word(word_dict))
        elif a == 'show_all_word': # Show all words #Alle Wörter anzeigen #Показати всі слова
            pprint(word_dict)
        else: # Command not found #Befehl nicht gefunden #Команду не знайдено
            print('Command not found\n') #Befehl nicht gefunden\n #Команду не знайдено\n

if __name__ == '__main__':
    main()



