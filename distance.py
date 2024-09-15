def save_bio_user_id(nomer):
    text = 'input'  # фраза, которая будет дописана в конец строки
    output = ''  # инициализация результирующего текста

    with open('1.txt', 'r') as file:
        for line in file:  # считывание текущего файла
            output += (line.replace('\n', '') + text + '\n')

    with open('1.txt', 'w') as file:
        file.write(output)  # перезапись файла


save_bio_user_id('fghfg')

with open('../bio_id', 'r') as file:
    for line in file:  # считывание текущего файла
        print(line.split('***'))