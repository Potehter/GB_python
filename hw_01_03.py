''' Определить, какие из слов 
«attribute», «класс», «функция», «type» 
невозможно записать в байтовом типе.'''
def main():
    start_list = ["attribute", "класс", "функция", "type"]
    for word in start_list:
        try:
            encode_word = bytes(word, 'ascii')
        except:
            print('Word: {0} cannot be written in bytes'.format(word))


if __name__ == '__main__':
    main()