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

def main():

    converter = IntegerToRomanConverter()


    try:
        number = int(input("Digite um número inteiro para conversão (1-3999): "))
        if number < 1 or number > 3999:
            raise ValueError("O número deve estar entre 1 e 3999.")
        
       
        roman_number = converter.integer_to_roman(number)
        print(f"O número inteiro {number} é o mesmo a '{roman_number}' em números romanos.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
