cipher_type = input('1) Ceaser Cipher\n'
                    '2) Substitution Cipher\n'
                    '3) Baconian Cipher\n'
                    '4) RailFence Cipher\n'
                    '5) Ultimate Cipher\n'
                    '6) Morse Code\n'
                    'choose the decipher type and enter the option number: ')
if cipher_type == '5':
    key = input(str('Enter the Key_text: '))
    key = key.upper()
while cipher_type in ['1', '4']:
    key = input('Enter the key(integer):')
    try:
        key = int(key)
    except ValueError:
        print('error: the input is not an integer')
        exit()

text = input('Enter the text: ')
text = text.upper() 

a = ['Q','W','E','R','T','Y',',','U','?','I','O','0','P','1','A',
         '2','S','3','D','4','F','5','G','6','H','7','J','8','K','9',
         'L','.','Z',"'",'X','C','V','B','N','M',' ']

def ceaser_cipher(text, key):
    #This cipher type shifts the letter position to the right or left based on the value of the key
    encryption = []
    key_sign = input('key is pos or neg?')
    for i in range(len(text)):
        for j in range(len(a)):
            if text[i] == a[j]:
                if key_sign == 'pos' or 'positive' or '+':
                    encrypted_index = (j + key) % len(a)
                    encryption.append(a[encrypted_index])
                elif key_sign == 'neg' or 'negative' or '-':
                    encrypted_index = (j - key) % len(a)
                    encryption.append(a[encrypted_index])
                else:
                    print('Enter valid key sign')
                    exit()
    encrypted_message = ''.join(encryption)
    return encrypted_message

def substitution_cipher(text):
    #This cypher type switches or substitutes the value of a letter to another letter
    encryption = []
    for i in range(len(text)):
        for j in range(len(a)):
            if text[i] == a[j]:
                new_letter = a[-j]
                encryption.append(new_letter)
    encrypted_message = ''.join(encryption)
    return encrypted_message

def baconian_cipher(text):
    #This cipher type converts text to binary values
    encryption= []
    char_to_binary = {a[i]: format(i, '05b') for i in range(len(a))}
    for char in text:
        if char in char_to_binary:
            encryption.append(char_to_binary[char])
        else:
            print('invalid text')
            exit()
    encrypted_message = ' '.join(encryption)
    return encrypted_message

def railfence_cipher(text, key):

    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    encryption = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                encryption.append(rail[i][j])
    return("" . join(encryption))

def ultimate_cipher(text, key):
    shift = []
    for i in range(len(key)):
        for j in range(len(a)):
            if key[i] == a[j]:
                index = a.index(a[j])
                shift.append(index)
    encryption = []
    for k in range(len(text)):
        encryption_index = (a.index(text[k]) + shift[k % len(shift)]) % len(a)
        encryption.append(a[encryption_index])

    encrypted_message = ''.join(encryption)
    return encrypted_message

def morse_code(text):
    morse_code_dict = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    encryption = ''
    for letter in text:
        if letter != ' ':
            encryption += morse_code_dict[letter] + ' '
        else:
            encryption += ' '
    return encryption


if cipher_type == '1':
    encrypted_message = ceaser_cipher(text, key) 
    print(encrypted_message)   
elif cipher_type == '2':
    encrypted_message = substitution_cipher(text)
    print(encrypted_message)                  
elif cipher_type == '3':
    encrypted_message = baconian_cipher(text)
    print(encrypted_message)
elif cipher_type == '4':
    encrypted_message = railfence_cipher(text, key)
    print(encrypted_message)
elif cipher_type == '5':
    encrypted_message = ultimate_cipher(text, key)
    print(encrypted_message)
elif cipher_type == '6':
    encrypted_message = morse_code(text)
    print(encrypted_message)



