
from tkinter import *

class MorseConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Morse Converter")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        # Morse codes of letters and numbers
        self.letters = ["·-", "-···", "-·-·", "-··", "·", "··-·", "--·", "····", "··", "·---", "-·-", "·-··", "--", "-·",
                        "---", "·--·", "--·-", "·-·", "···", "-", "··-", "···-", "·--", "-··-", "-·--", "--··"]

        self.numbers = ["-----", "·----", "··---", "···--", "····-", "·····", "-····", "--···", "---··", "----·"]

        self.input_label = Label(window, text="Enter Text: ", font=("Arial", 16))
        self.input_label.place(x=50, y=50)

        self.input_entry = Entry(window, font=("Arial", 16), width=35)
        self.input_entry.place(x=200, y=50)
        self.input_entry.bind('<KeyRelease>', self.convert) 
        # bind the convert method to the KeyRelease event so that the conversion is done automatically when the user types in the input field

        self.output_label = Label(window, text="Morse Code: ", font=("Arial", 16))
        self.output_label.place(x=50, y=100)

        self.output_entry = Entry(window, font=("Arial", 16), width=35)
        self.output_entry.place(x=200, y=100)

    def is_letter(self, ch): # helper method to check if a character is a letter
        if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
            return True
        return False

    def convert(self, event=None): # method to convert the input text to Morse code
        word = self.input_entry.get()
        answer = ""
        for c in word:
            if c.isnumeric(): # check if the character is a positive number
                idx = ord(c) - ord('0')
                answer += self.numbers[idx]
                answer += "/"
            elif self.is_letter(c): # check if the character is a letter
                idx = ord(c.upper()) - ord('A')
                answer += self.letters[idx]
                answer += "/"
            elif c==' ': # check if the character is a space
                answer += "/"
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, answer)
        
    