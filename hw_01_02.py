'''Каждое из слов «class», «function», «method» 
записать в байтовом типе без преобразования в последовательность 
кодов (не используя методы encode и decode) и определить тип, 
содержимое и длину соответствующих переменных.'''
def main():
    start_list = [b'class', b'function', b'method']
    for word in start_list:
        print('type: {0}, word: {1}, length: {2}'.format(
            type(word), word, len(word)))


if __name__ == '__main__':
    main()