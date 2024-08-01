import tkinter as tk
from tkinter import messagebox

class RomanToIntegerConverter:
    def __init__(self):
        self.roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_integer(self, roman):
        roman = roman.upper()
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_to_int.get(char, 0)
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total

class IntegerConverterApp:
    def __init__(self, root):
        self.converter = RomanToIntegerConverter()
        self.root = root
        self.root.title("Conversor de Números Romanos para Inteiros")

        self.label = tk.Label(root, text="Digite um número romano:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.convert_button = tk.Button(root, text="Converter", command=self.convert)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def convert(self):
        roman = self.entry.get()
        if all(char in 'IVXLCDM' for char in roman.upper()):
            integer = self.converter.roman_to_integer(roman)
            self.result_label.config(text=f"Equivalente em inteiro: {integer}")
        else:
            messagebox.showerror("Erro", "Digite um número romano válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IntegerConverterApp(root)
    root.mainloop()
