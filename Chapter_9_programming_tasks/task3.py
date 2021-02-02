def encrypt_file():
    cipher_dict = {'А': '$', 'а': '%', 'Б': '#', 'б': '@', 'В': '!', 'в': '^', 'Г': '&', 'г': '*', 'Д': '(', 'д': ')',
                   'Е': '-', 'е': '_', 'Ё': '+', 'ё': '=', 'Ж': '/', 'ж': '?', 'З': '>', 'з': '<', 'И': 'z', 'и': 'x',
                   'Й': 'c', 'й': 'v', 'К': 'b', 'к': 'n', 'Л': 'm', 'л': '"', 'М': ';', 'м': ':', 'Н': 'l', 'н': 'h',
                   'О': 'j', 'о': 'g', 'П': 'f', 'п': 'd', 'Р': 's', 'р': 'a', 'С': ']', 'с': '[', 'Т': '}', 'т': '{',
                   'У': 'p', 'у': 'o', 'Ф': 'i', 'ф': 'u', 'Х': 'y', 'х': 't', 'Ц': 'r', 'ц': 'e', 'Ч': 'w', 'ч': 'q',
                   'Ш': 'Z', 'ш': 'X', 'Щ': 'C', 'щ': ' V', 'ъ': 'B', 'ы': 'N', 'ь': 'M', 'Э': 'A', 'э': 'S', 'Ю': 'D',
                   'ю': 'F', 'Я': 'G', 'я': 'H'}
    read_file_text = open('free_text.txt', 'r')
    line = read_file_text.readline()
    temp_read_symbol = []
    for symbol in line:
        if symbol in cipher_dict:
            temp_read_symbol.append(cipher_dict[symbol])
        else:
            temp_read_symbol.append(symbol)
    temp_symbol_string = ''.join(temp_read_symbol)
    print(temp_symbol_string)

    cipher_text = open("cipher_text.txt", "w")
    cipher_text.write(temp_symbol_string)

def decrypt_file():
    cipher_dict = {'А': '$', 'а': '%', 'Б': '#', 'б': '@', 'В': '!', 'в': '^', 'Г': '&', 'г': '*', 'Д': '(', 'д': ')',
                   'Е': '-', 'е': '_', 'Ё': '+', 'ё': '=', 'Ж': '/', 'ж': '?', 'З': '>', 'з': '<', 'И': 'z', 'и': 'x',
                   'Й': 'c', 'й': 'v', 'К': 'b', 'к': 'n', 'Л': 'm', 'л': '"', 'М': ';', 'м': ':', 'Н': 'l', 'н': 'h',
                   'О': 'j', 'о': 'g', 'П': 'f', 'п': 'd', 'Р': 's', 'р': 'a', 'С': ']', 'с': '[', 'Т': '}', 'т': '{',
                   'У': 'p', 'у': 'o', 'Ф': 'i', 'ф': 'u', 'Х': 'y', 'х': 't', 'Ц': 'r', 'ц': 'e', 'Ч': 'w', 'ч': 'q',
                   'Ш': 'Z', 'ш': 'X', 'Щ': 'C', 'щ': ' V', 'ъ': 'B', 'ы': 'N', 'ь': 'M', 'Э': 'A', 'э': 'S', 'Ю': 'D',
                   'ю': 'F', 'Я': 'G', 'я': 'H'}
    read_cipher_text = open('cipher_text.txt', 'r')
    line = read_cipher_text.readline()
    temp_read_symbol = []
    for symbol in line:
        for key, value in cipher_dict.items():
            if value == symbol:
                temp_read_symbol.append(key)
        if symbol not in cipher_dict.values():
            temp_read_symbol.append(symbol)
    temp_symbol_string = ''.join(temp_read_symbol)
    print(temp_symbol_string)

encrypt_file()
decrypt_file()