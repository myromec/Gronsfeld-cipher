rus = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') # Русский алфавит
eng = list('abcdefghijklmnopqrstuvwxyz') # Английский алфавит

input_user = input('Enter the word you want to encrypt: ') # Выписываем слово, которое нам нужно зашифровать
key_user = input('Enter the key you want to use: ') # Выписываем ключ, которым мы будем шифровать

result = "" # Пустая строка, в которую будет записан результат
for i in range(len(input_user)): # Создаем цикл который будет высчитывать длину слова
    ch = input_user[i] # Добавляем к некоторой переменной буквы
    if ch in rus: # Если эта буква есть в русском алфавите:
        key = rus.index(ch)  # берем индекс нужной буквы
        shift = int(key_user[i % len(key_user)])  # берём цифру ключа
        perenos = (key + shift) % len(rus) # Переменная, в которой записано число, на которое нужно сместить индекс, чтоб зашифровать слово
        result += rus[perenos] # В переменную результат добавляем зашифрованную букву
    elif ch in eng: # если эта буква есть в английском алфавите то:
        key = eng.index(ch) # Берем индекс данной буквы
        shift = int(key_user[i % len(key_user)]) # берем цифру ключа
        perenos = (key + shift) % len(eng)  # Переменная, в которой записано число, на которое нужно сместить индекс, чтоб зашифровать слово
        result += eng[perenos] # В переменную результат добавляем зашифрованную букву
    else:
        result += ch  # если это пробел или символ, просто добавляем

print("encrypted word:", result)
