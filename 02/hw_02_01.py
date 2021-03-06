'''1. Задание на закрепление знаний по модулю CSV. 
Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл 
в формате CSV. Для этого: Создать функцию get_data(), 
в которой в цикле осуществляется перебор файлов с данными, 
их открытие и считывание данных. В этой функции из считанных данных 
необходимо с помощью регулярных выражений извлечь значения параметров 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 
Значения каждого параметра поместить в соответствующий список. 
Должно получиться четыре списка — 
например, os_prod_list, os_name_list, os_code_list, os_type_list. 
В этой же функции создать главный список для хранения данных отчета
например, main_data — и поместить в него названия столбцов отчета 
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», 
«Тип системы». Значения для этих столбцов также оформить в виде списка 
и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().'''
import csv
import re
files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
def get_data():
    main_data = [['Изготовитель системы',
    'Название ОС',
    'Код продукта',
    'Тип системы'
    ]]
    regex_list = [r"Изготовитель системы:\s*\w*", 
         r"Название ОС:\s*\w*",
         r"Код продукта:\s*\w*",
         r"Тип системы:\s*\w*"]
    for each_file in files_list:
        new_elem = []
        with open(each_file, encoding='cp1251') as file:
            test = file.readlines()
        for case in regex_list:
            result = re.findall(case, str(test))
            new_elem.append(result[0].split()[-1])
        main_data.append(new_elem)
    return main_data

def write_to_csv(file_name):
    write_data = get_data()
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        for row in write_data:
            writer.writerow(row)
        

def main():
    write_to_csv('test.csv')

if __name__ == '__main__':
    main()