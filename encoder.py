from __init__ import *

class Encoder:
    @staticmethod
    def enc():
        while True:
            b = input('Enter the text to encrypt: \n')
            if b == '':
                print('{}{}'.format(Bcolors.R, "Blank input!"))
                continue

            if len(encoder1) != len(set('{}{}'.format(b, encoder1))):
                print('{}{}'.format(Bcolors.R, 'No characters found in the key!'))
                continue
            print('{}{}{}'.format(Bcolors.G, '\n', 'Encrypted text:\n'))

            i = 1
            
            for c in b:
                encoder = ''
                y = encoder1.index(c)
                if i % 3 == 0:
                    encoder += encoder4[y] + random.choice(encoder2)
                elif i % 2 == 0:
                    encoder += encoder3[y]
                else:
                    encoder += encoder2[y]
                i += 1
                print(encoder, end="")
            print()
            break