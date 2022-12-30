# Читаем текстового файла с предсказаниями и создание из него файла фикстур
# файл в формте JSON для записи данных в модель
# python manage.py loaddata fixture_prediction.json
import sys, os
import json


input_file = os.path.join(sys.path[0], 'predictions_new.txt')  # Файл ввода
output_file = os.path.join(sys.path[0], 'fixture_prediction.json')  # Файл вывода

with open(input_file, 'r', encoding='utf-8') as f:
    all_string = f.readlines()

string_out = []
for i, string in enumerate(all_string, 1):
    string = string.strip()
    record = dict()
    record['model'] = 'happy_new_year.prediction'
    record['pk'] = i
    record['fields'] = {'prediction': string}
    string_out.append(record)


with open(output_file, 'w') as f:
    f.write(json.dumps(string_out, indent=2))


