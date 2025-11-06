rus = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') # Русский алфавит
eng = list('abcdefghijklmnopqrstuvwxyz') # Английский алфавит

input_user = input('Введите слово которое хотите зашифровать: ') #  переменная, в которую будет записано слово
key = input('Введите ключ которым будет зашифровано слово: ')
cipher = ''
for i,m in enumerate(input_user):
    
    if m in rus:
        index_input = rus.index(m)
    k = key[i % len(key)] 
    index_key = rus.index(k)
    
    cipher += rus[(index_input + index_key) % len(rus)]
print(cipher)



