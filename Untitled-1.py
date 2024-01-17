def leet_speak(text):
    leet_table = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': '\/\/',
        'n': '^/',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': '\/',
        'w': '\/\/',
        'x': '><',
        'y': 'j',
        'z': '2',
        '1': 'L',
        '2': 'R',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'b',
        '7': 'T',
        '8': 'B',
        '9': 'g',
        '0': 'o'

    }

    leet_text = ""
    for char in text:
        if char.lower() in leet_table:
            leet_text += leet_table[char.lower()]
        else:
            leet_text += char

    return leet_text

# Ejemplo de uso
texto_original = input("Ingrese un texto: ")
texto_en_leet = leet_speak(texto_original)
print("Texto en leet speak:", texto_en_leet)
