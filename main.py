
import tkinter as tk
from interface import MorseConverter


def main():
    
    window = tk.Tk()
    morseConverter = MorseConverter(window)
    window.mainloop()
    

if __name__ == "__main__":
    
    main()
    
