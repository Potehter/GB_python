'''Создать текстовый файл test_file.txt, 
заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое.'''
def main():
    start_list = ["сетевое программирование", "сокет", "декоратор"]
    with open('test_file.txt', 'w') as test_file:
        for word in start_list:
            test_file.write(word + '\n')

    with open('test_file.txt', 'r', encoding='utf-8') as test_file:
        print(test_file.read())


if __name__ == '__main__':
    main()