# language_translator.py
from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import messagebox

# Initialize translator
translator = Translator()

# Function to perform translation
def translate_text():
    try:
        input_text = input_box.get("1.0", END).strip()
        src_lang = lang_codes[src_lang_var.get()]
        dest_lang = lang_codes[dest_lang_var.get()]
        translated = translator.translate(input_text, src=src_lang, dest=dest_lang)
        output_box.delete("1.0", END)
        output_box.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy text function
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_box.get("1.0", END).strip())
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# Create main window
root = Tk()
root.title("🌐 Language Translation Tool")
root.geometry("600x400")

# Language dropdown options
lang_codes = {lang.title(): code for code, lang in LANGUAGES.items()}
languages = sorted(lang_codes.keys())

# Language Selection
Label(root, text="Source Language").grid(row=0, column=0, padx=10, pady=10)
src_lang_var = StringVar(root)
src_lang_var.set("English")
OptionMenu(root, src_lang_var, *languages).grid(row=0, column=1)

Label(root, text="Target Language").grid(row=0, column=2)
dest_lang_var = StringVar(root)
dest_lang_var.set("Hindi")
OptionMenu(root, dest_lang_var, *languages).grid(row=0, column=3)

# Input Text Box
Label(root, text="Enter Text").grid(row=1, column=0, padx=10, pady=10)
input_box = Text(root, height=5, width=70)
input_box.grid(row=2, column=0, columnspan=4, padx=10)

# Translate Button
Button(root, text="Translate", command=translate_text, bg="green", fg="white").grid(row=3, column=1, pady=10)

# Output Text Box
Label(root, text="Translated Text").grid(row=4, column=0, padx=10, pady=10)
output_box = Text(root, height=5, width=70)
output_box.grid(row=5, column=0, columnspan=4, padx=10)

# Copy Button
Button(root, text="Copy", command=copy_text).grid(row=6, column=1, pady=10)

root.mainloop()
import pyttsx3

def speak_output():
    engine = pyttsx3.init()
    engine.say(output_box.get("1.0", END).strip())
    engine.runAndWait()
Button(root, text="🔊 Speak", command=speak_output).grid(row=6, column=2)
