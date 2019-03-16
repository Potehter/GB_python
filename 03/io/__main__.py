with open('io/text_read.txt') as file:
    print(file.readlines())

with open('io/text_write.txt', 'w') as file:
    file.write('Some content')
