# Читаем файл с предсказаниями удаление переносов, где следующаястрока начинается с маленькой буквы
# и удаление цифр
import sys, os
import re


input_file = os.path.join(sys.path[0], 'predictions.txt')  # Файл ввода
output_file = os.path.join(sys.path[0], 'predictions_new.txt')  # Файл вывода

with open(input_file, 'r', encoding='utf-8') as f:
    all_words = f.readlines()

with open(output_file, 'w', encoding='utf-8') as f:
    string_out = ''
    for string in all_words:
        string = string.strip()
        string = re.sub("\d+", "", string)
        if string[0].islower():
            string_out += ' ' + string
        else:
            if string_out:
                f.write(string_out + '\n')
            string_out = string

    f.write(string_out)