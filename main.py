# main.py
#yyy
import tkinter as tk
from tkinter import Label, messagebox, simpledialog, filedialog
from random import shuffle
import random
import json

from database.models import Dictionary
from database.db import get_session, create_tables

# Create the tables if they do not exist
create_tables()

# Get a new session
session = get_session()

# Variable to track language mode (default: de->en)
language_mode = "de_to_en"

# Function to check if there are words in the database
def words_in_db():
    return session.query(Dictionary).count() > 0

# Variable to track whether a correct answer has been provided
correct_answer_provided = False

# Function to select random words from the database
def get_random_words():
    words = session.query(Dictionary).all()
    if len(words) < 4:
        messagebox.showerror("Error", "Not enough words in the database.")
        return []
    return random.sample(words, 4)

# Function to change the text on the label and the color of the button
def change_text(correct_answer, button_texts, num: int):
    global correct_answer_provided  # Accessing the global variable
    if (language_mode == "de_to_en" and button_texts[num].en == correct_answer) or \
       (language_mode == "en_to_de" and button_texts[num].de == correct_answer):
        buttons[num]['background'] = "#13f24b"  # Green color for the correct answer
        correct_answer_provided = True  # Mark that a correct answer was provided
        button5.pack(pady=20)  # Show the "Retake Quiz" button
    else:
        buttons[num]['background'] = "#f21b13"  # Red color for the wrong answer

# Function to reset the quiz text
def widerholen_text():
    global correct_answer_provided  # Accessing the global variable
    button_texts = get_random_words()  # Get 4 random elements from the database
    if not button_texts:
        return
    
    if language_mode == "de_to_en":
        correct_answer = button_texts[0].en  # Correct answer in English
        label["text"] = button_texts[0].de  # Question in German
    else:
        correct_answer = button_texts[0].de  # Correct answer in German
        label["text"] = button_texts[0].en  # Question in English
    
    shuffle(button_texts)
    # Update button texts and reset their colors
    for i in range(4):
        if language_mode == "de_to_en":
            buttons[i]['text'] = button_texts[i].en  # Buttons with answers in English
        else:
            buttons[i]['text'] = button_texts[i].de  # Buttons with answers in German
        
        buttons[i]['background'] = "SystemButtonFace"  # Reset button color to default
        # Update button commands
        buttons[i]['command'] = lambda i=i: change_text(correct_answer, button_texts, i)
    
    correct_answer_provided = False  # Reset the correct answer flag
    button5.pack_forget()  # Hide the retake quiz button

# Function to switch to "Settings" mode
def open_settings():
    hide_quiz_buttons()  # Hide quiz buttons
    add_word_button.pack(side=tk.TOP, pady=10, padx=10)
    update_word_en_button.pack(side=tk.TOP, pady=10, padx=10)
    update_word_de_button.pack(side=tk.TOP, pady=10, padx=10)
    switch_language_button.pack(side=tk.TOP, pady=10, padx=10)
    delete_word_button.pack(side=tk.TOP, pady=10, padx=10)
    load_json_button.pack(side=tk.TOP, pady=10, padx=10)
    return_button.pack(side=tk.BOTTOM, pady=10)

# CRUD functions to manage the dictionary
def add_word():
    en_word = simpledialog.askstring("Add Word", "Enter an English word:")
    de_word = simpledialog.askstring("Add Word", "Enter a German word:")
    if en_word and de_word:
        existing_word = session.query(Dictionary).filter_by(en=en_word).first()
        if existing_word:
            messagebox.showerror("Error", f"The word '{en_word}' already exists in the database!")
        else:
            new_word = Dictionary(en=en_word, de=de_word)
            session.add(new_word)
            session.commit()
            messagebox.showinfo("Success", f"The word '{en_word} - {de_word}' has been successfully added!")
    else:
        messagebox.showerror("Error", "You must enter both words.")

def update_word_en():
    en_word = simpledialog.askstring("Update English Word", "Enter the English word to update:")
    word = session.query(Dictionary).filter_by(en=en_word).first()
    if word:
        new_de_word = simpledialog.askstring("Update English Word", f"Enter the new German translation for '{en_word}':")
        if new_de_word:
            existing_word = session.query(Dictionary).filter_by(de=new_de_word).first()
            if existing_word:
                messagebox.showerror("Error", f"The translation '{new_de_word}' is already used for another word!")
            else:
                word.de = new_de_word
                session.commit()
                messagebox.showinfo("Success", f"The word '{en_word}' has been successfully updated!")
    else:
        messagebox.showerror("Error", "Word not found.")

def update_word_de():
    de_word = simpledialog.askstring("Update German Word", "Enter the German word to update:")
    word = session.query(Dictionary).filter_by(de=de_word).first()
    if word:
        new_en_word = simpledialog.askstring("Update German Word", f"Enter the new English translation for '{de_word}':")
        if new_en_word:
            existing_word = session.query(Dictionary).filter_by(en=new_en_word).first()
            if existing_word:
                messagebox.showerror("Error", f"The translation '{new_en_word}' is already used for another word!")
            else:
                word.en = new_en_word
                session.commit()
                messagebox.showinfo("Success", f"The word '{de_word}' has been successfully updated!")
    else:
        messagebox.showerror("Error", "Word not found.")

def delete_word():
    en_word = simpledialog.askstring("Delete Word", "Enter the English word to delete:")
    word = session.query(Dictionary).filter_by(en=en_word).first()
    if word:
        session.delete(word)
        session.commit()
        messagebox.showinfo("Success", f"The word '{en_word}' has been successfully deleted!")
    else:
        messagebox.showerror("Error", "Word not found.")

def load_words_from_json():
    json_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON Files", "*.json")])
    if json_path:
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                added_words = 0
                for entry in data:
                    en_word = entry.get('en')
                    de_word = entry.get('de')
                    if en_word and de_word:
                        existing_word = session.query(Dictionary).filter_by(en=en_word).first()
                        if not existing_word:
                            new_word = Dictionary(en=en_word, de=de_word)
                            session.add(new_word)
                            added_words += 1
                session.commit()
                messagebox.showinfo("Success", f"Successfully added {added_words} words from the file!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the file: {e}")
    else:
        messagebox.showwarning("Warning", "No file was selected.")

# Function to switch the question/answer language
def switch_language():
    global language_mode
    if language_mode == "de_to_en":
        language_mode = "en_to_de"
    else:
        language_mode = "de_to_en"
    widerholen_text()  # Reload the quiz with new language mode

# Hide quiz buttons
def hide_quiz_buttons():
    label.pack_forget()  # Hide the question label
    for button in buttons:
        button.pack_forget()
    button5.pack_forget()
    settings_button.pack_forget()  # Hide the settings button

# Return to quiz mode
def return_to_quiz():
    # Hide setting buttons
    add_word_button.pack_forget()
    update_word_en_button.pack_forget()
    update_word_de_button.pack_forget()
    switch_language_button.pack_forget()
    delete_word_button.pack_forget()
    load_json_button.pack_forget()
 
    return_button.pack_forget()

    # Show quiz buttons
    label.pack(pady=20)  # Show question label
    for button in buttons:
        button.pack(pady=5)  # Show answer buttons
    settings_button.pack(side=tk.BOTTOM, pady=10)  # Show settings button

    widerholen_text()  # Start a new quiz

# Create main window
root = tk.Tk()
root.title("Language Testing App")
root.geometry("250x500")

# Create and place label for the question
label = Label(root, text="", font=("Helvetica", 20))
label.pack(pady=20)

# Create buttons for answers
buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=20, height=2)  # Set fixed width and height
    button.pack(pady=5)
    buttons.append(button)

# Create "Retake Quiz" button
button5 = tk.Button(root, text="Retake Quiz", width=20, height=2, command=widerholen_text, font=("Arial", 15))  # Set fixed width and height
button5.pack_forget()  # Initially hidden

# Create "Settings" button
settings_button = tk.Button(root, text="Settings", width=20, height=2, command=open_settings, font=("Arial", 15))  # Set fixed width and height
settings_button.pack(side=tk.BOTTOM, pady=20)

# Create settings buttons
add_word_button = tk.Button(root, text="Add Word", width=20, height=2, command=add_word, font=("Arial", 10))
update_word_en_button = tk.Button(root, text="Update English Word", width=20, height=2, command=update_word_en, font=("Arial", 10))
update_word_de_button = tk.Button(root, text="Update German Word", width=20, height=2, command=update_word_de, font=("Arial", 10))
switch_language_button = tk.Button(root, text="Switch Language", width=20, height=2, command=switch_language, font=("Arial", 10))
delete_word_button = tk.Button(root, text="Delete Word", width=20, height=2, command=delete_word, font=("Arial", 10))
load_json_button = tk.Button(root, text="Load Words from JSON", width=20, height=2, command=load_words_from_json, font=("Arial", 10))
return_button = tk.Button(root, text="Return to Quiz", width=20, height=2, command=return_to_quiz, font=("Arial", 15))

# Start the first quiz
widerholen_text()

# Start the main loop
root.mainloop()


