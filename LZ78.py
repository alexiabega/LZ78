def encodeLZ(FileIn, FileOut):
    input_file = open(FileIn, 'r')
    encoded_file = open(FileOut, 'w')
    text_from_file = input_file.read()
    dict_of_codes = {text_from_file[0]: '1'}
    encoded_file.write('0' + text_from_file[0])
    text_from_file = text_from_file[1:]
    combination = ''
    code = 2
    counter = 0

    for char in text_from_file:
        combination += char
        if combination not in dict_of_codes:
            dict_of_codes[combination] = str(code)
            if len(combination) == 1:
                encoded_file.write('0' + combination)
                counter += 1
            else:
                encoded_file.write(dict_of_codes[combination[0:-1]] + combination[-1])
            code += 1
            combination = ''
    input_file.close()
    encoded_file.close()
    print("encoding counter", counter)
    return True


def decodeLZ(FileIn, FileOut):
    coded_file = open(FileIn, 'r')
    decoded_file = open(FileOut, 'w')
    text_from_file = coded_file.read()
    dict_of_codes = {'0': '', '1': text_from_file[1]}
    decoded_file.write(dict_of_codes['1'])
    text_from_file = text_from_file[2:]
    combination = ''
    code = 2
    counter = 0

    for char in text_from_file:
        if char in '1234567890':
            combination += char
            counter += 1
            print("decoding counter", counter)
        else:
            dict_of_codes[str(code)] = dict_of_codes[combination] + char
            decoded_file.write(dict_of_codes[combination] + char)
            combination = ''
            code += 1
    coded_file.close()
    decoded_file.close()


f1 = open("backwards.txt", "w")
with open("english.txt", "r") as myfile:
    data = myfile.read()
data_1 = data[::-1]
f1.write(data_1)
f1.close()



encodeLZ('english.txt', 'encoded.txt')
encodeLZ('backwards.txt', 'encoded.txt')
decodeLZ('encoded.txt', 'decoded.txt')


