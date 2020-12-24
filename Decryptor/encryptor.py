
import random

def manuallySetkey():
    print('input key:')
    new_key = input()
    print('key updated: ', new_key)
    return new_key

def setRandomKey(key):
    l = list(key)
    random.shuffle(l)
    key = ''.join(l)
    print('random key is: ', key)
    return key

def encryptText(key):
    print('')
    print('current key:')
    print(key)
    print('')
    print('enter text:')
    text = input()
    output = ''
    for c in text:
        if not c.isalpha():
            output += c
        else:
            c = c.lower()
            output += key[ord(c) - ord('a')]
    print('')
    print('encrypted text is:')
    print(output)


def ask4instructions():
    # this key doesn't change anything
    key = 'abcdefghikjlmnopqrstuvwxyz'

    while True:
        print('')
        print('1 - manually set key')
        print('2 - set random key')
        print('3 - generate encrypted text')
        print('q - quit')
        print('')
        print('your input:')
        inp  = input()
        if inp == 'q':
            break
        elif inp == '1':
            key = manuallySetkey()
        elif inp == '2':
            key = setRandomKey(key)
        elif inp == '3':
            encryptText(key)
        else:
            print('invalid input')
            print(' ')

        


if __name__ == '__main__':
    ask4instructions()