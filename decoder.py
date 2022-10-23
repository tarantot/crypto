from __init__ import *

class Decoder:
    @staticmethod
    def dec():
        while True:
            m = input('{}{}'.format('Enter the text to decrypt: ', '\n'))
            if m == '':
                print('{}{}'.format(Bcolors.R, "Blank input!"))
                continue

            t = m + encoder2
            if len(encoder2) != len(set(t)):
                print('{}{}'.format(Bcolors.R, 'No characters found in the key!'))
                continue
            print('{}{}{}'.format(Bcolors.G, '\n', 'Decrypted text:\n'))

            i = 1
            m = ''.join(m [i : i + 3] for i in range(0, len(m), 4))
            for x in m:
                decoder = ''
                if i % 3 == 0:
                    y = encoder4.index(x)
                    decoder += encoder1[y]
                elif i % 2 == 0:
                    y = encoder3.index(x)
                    decoder += encoder1[y]
                else:
                    y = encoder2.index(x)
                    decoder += encoder1[y]
                i += 1
                print(decoder, end="")
            print()
            break