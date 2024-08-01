class RomanConverter:
    def __init__(self):
        
        self.roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_integer(self, roman):
        
        total = 0
        prev_value = 0

        for char in reversed(roman.upper()):
            value = self.roman_to_int.get(char, 0)
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

def main():
    
    converter = RomanConverter()

   
    roman_number = input("Digite um número romano para conversão: ")

    
    try:
        integer_number = converter.roman_to_integer(roman_number)
        print(f"O número romano '{roman_number}' é o mesmo a {integer_number} em números inteiros.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
