import json # Импорт модуля для работы с файлами в формате JSON
import random # Импорт модуля для работы с генерацией случайных чисел

if __name__ == '__main__':
    with open('adjective.json') as f: # открывается файл с прилагательными как список
        adjective = json.loads(f.read()) # преобразуем в python список
    with open('noun.json') as f: # открывается файл с существительными как список
        noun = json.loads(f.read()) # преобразуем в python список

    with open('output.txt', 'w', encoding='utf-8') as f: # открываем файл для записи сгенерированных никнеймов (output.txt)
        for i in range(5): # генерируется 5 ников
            f.write(adjective[random.randrange(len(adjective)-1)]+' '+noun[random.randrange(len(noun)-1)] + '\n') # Выбираем случайное прилагательное и случайное существительное
