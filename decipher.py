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
text = input('Enter the text:')
if cipher_type == '3':
    text = text.split()
else:
    text = text.upper()

a = ['Q','W','E','R','T','Y',',','U','?','I','O','0','P','1','A',
     '2','S','3','D','4','F','5','G','6','H','7','J','8','K','9',
     'L','.','Z',"'",'X','C','V','B','N','M',' ']

def ceaser_decipher(text, key):
    
    decryption = []
    key_sign = input('key is pos or neg?')
    for i in range(len(text)):
        for j in range(len(a)):
            if text[i] == a[j]:
                if key_sign == 'pos' or 'positive' or '+':
                    encrypted_index = (j - key) % len(a)
                    decryption.append(a[encrypted_index])
                elif key_sign == 'neg' or 'neg' or '-':
                    encrypted_index = (j + key) % len(a)
                    decryption.append(a[encrypted_index])
                else:
                    print('Enter valid key sign')
                    exit()
    decrypted_message = ''.join(decryption)
    return decrypted_message

def substitution_decipher(text):
    
    decryption = []
    for i in range(len(text)):
        for j in range(len(a)):
            if text[i] == a[j]:
                new_letter = a[-j]
                decryption.append(new_letter)
    decrypted_message = ''.join(decryption)
    return decrypted_message

def baconian_decipher(text):
   
    binary_list = text
    decryption= []
    binary_to_char = {format(i, '05b'): a[i] for i in range(len(a))}
    for binary in binary_list:
        if binary in binary_to_char:
            decryption.append(binary_to_char[binary])
        else:
            print('invalid text')
            exit()
    decrypted_message = ''.join(decryption)
    return decrypted_message

def railfence_decipher(text, key):
 
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if ((rail[i][j] == '*') and
            (index < len(text))):
                rail[i][j] = text[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

def ultimate_decipher(text, key):
    shift = []
    for i in range(len(key)):
        for j in range(len(a)):
            if key[i] == a[j]:
                index = a.index(a[j])
                shift.append(index)
    decryption = []
    for k in range(len(text)):
        decryption_index = (a.index(text[k]) - shift[k % len(shift)]) % len(a)
        decryption.append(a[decryption_index])

    decrypted_message = ''.join(decryption)
    return decrypted_message

def morsecode_decipher(text):
    morse_code_dict = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':' '}
 
    text += ' '
 
    decipher = ''
    citext = ''
    for letter in text:
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(morse_code_dict.keys())[list(morse_code_dict
                .values()).index(citext)]
                citext = ''
 
    return decipher

if cipher_type == '1':
    decrypted_message = ceaser_decipher(text, key)
    print(f'Decrypted Message: {decrypted_message}')   
elif cipher_type == '2':
    decrypted_message = substitution_decipher(text)
    print(f'Decrypted Message: {decrypted_message}')        
elif cipher_type == '3':
    decrypted_message = baconian_decipher(text)
    print(f'Decrypted Message: {decrypted_message}')
elif cipher_type == '4':
    decrypted_message = railfence_decipher(text, key)
    print(f'Decrypted Message: {decrypted_message}')
elif cipher_type == '5':
    decrypted_message = ultimate_decipher(text, key)
    print(f'Decrypted Message: {decrypted_message}')
elif cipher_type == '6':
    decrypted_message = morsecode_decipher(text)
    print(f'Decrypted Message: {decrypted_message}')

