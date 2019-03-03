'''Преобразовать слова «разработка», «администрирование», 
«protocol», «standard» из строкового представления 
в байтовое и выполнить обратное преобразование 
(используя методы encode и decode).'''
def main():
    start_list = ["разработка", "администрирование", 'protocol', 'standard']
    for word in start_list:
        encode_word = word.encode('utf-8')
        decode_word = encode_word.decode()
        print("Start word: {0}, after en/decoding: {1}".format(
              word, decode_word))


if __name__ == '__main__':
    main()