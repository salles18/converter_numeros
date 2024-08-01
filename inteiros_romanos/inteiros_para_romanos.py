import tkinter as tk
from tkinter import messagebox

class IntegerToRomanConverter:
    def __init__(self):
        self.int_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def integer_to_roman(self, num):
        roman = ''
        for value, numeral in self.int_to_roman:
            while num >= value:
                roman += numeral
                num -= value
        return roman

class RomanConverterApp:
    def __init__(self, root):
        self.converter = IntegerToRomanConverter()
        self.root = root
        self.root.title("Conversor de Números Inteiros para Romanos")

        self.label = tk.Label(root, text="Digite um número inteiro (1-3999):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.convert_button = tk.Button(root, text="Converter", command=self.convert)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def convert(self):
        try:
            num = int(self.entry.get())
            if 1 <= num <= 3999:
                roman = self.converter.integer_to_roman(num)
                self.result_label.config(text=f"Equivalente em romano: {roman}")
            else:
                messagebox.showerror("Erro", "Digite um número entre 1 e 3999.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RomanConverterApp(root)
    root.mainloop()
