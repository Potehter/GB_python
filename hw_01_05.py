'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
преобразовать результаты из байтовового в строковый тип на кириллице.'''
from telnetlib import Telnet
def main():
    with Telnet('yandex.ru', 80) as tn:
        print(tn.read_all())



if __name__ == '__main__':
    main()