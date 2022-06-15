class Task:

    def __init__(self): # добавил __
        self.input_data()

    def string_number(self): # убрал "a" из параметров
        # везде где есть "а" добавил self так как это внутреняя переменная класса
        vowels = "ауоыиэяюёе"
        consonants = "бвгджзйклмнпрстфхцчшщ"
        list_vowels = []
        list_consonants = []
        sum_even_digits = sum_even_numbers = 0
        counter = 0
        # if self.a == str(a):
        if self.a.isalpha():  # вот так нужно проверять на налаичие символов в строке

           # тут нужно доработать, пока не понятно
           for i in self.a:
                if i in vowels:
                    list_vowels.append(i)
                elif i in consonants:
                    list_consonants.append(i)
                    return len(list_vowels) * len(list_consonants)

        # elif a == int(a):
        elif self.a.isdigit(): # вот так нужно проверять на налаичие цифр в строке
            int_a = int(self.a) # добавил переменную и перевел её в число из строки

            # тут тоже пока не понял
            while int_a > 0:
                counter = counter + 1
                if counter % 2 == 0:
                    digit = int_a % 10
                    sum_even_numbers = sum_even_numbers + digit
                    int_a = int_a // 10
                    return sum_even_numbers

    def mixing(self):
        # if a == str:
        pass

    def input_data(self):
        self.a = input("Введите данные: ")


objectTask = Task()
print(objectTask.string_number())