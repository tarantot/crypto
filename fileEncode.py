from __init__ import *


class FileEncode:
    @staticmethod
    def file_enc():
        try:
            with open('main.txt', 'r', encoding='utf-8') as f:  # open the file main.txt
                new_data = f.read().replace("\r", "")
                f.seek(0, os.SEEK_END)  # jump to the end of the file
                if f.tell():  # if True 
                    f.seek(0)  # jump to the beginning
                else:  
                    print('{}{}{}'.format(Bcolors.R, Bcolors.U, 'File is empty!'))
                    return Options.choice()

                i = 1
                encoder = ''
                for c in new_data:
                    if c == '\n':
                        if i % 3 == 0:
                            encoder += '南' + random.choice(encoder2)
                            i += 1
                        else:
                            encoder += '南'
                            i += 1
                    elif c == '\t':
                        if i % 3 == 0:
                            encoder += '林' + random.choice(encoder2)
                            i += 1
                        else:
                            encoder += '林'
                            i += 1
                    elif len(set(c + encoder1)) != 171:
                        print('{}{}{}{}'.format(Bcolors.R, 'No characters found in the key! ', 'Missing character: ', c))
                        return Options.choice()
                    else:
                        y = encoder1.index(c)
                        if i % 3 == 0:
                            encoder += encoder4[y] + random.choice(encoder2)
                        elif i % 2 == 0:
                            encoder += encoder3[y]
                        else:
                            encoder += encoder2[y]
                        i += 1
                encoder = '\n'.join(encoder[ i : i + 26 ] for i in range(0, len(encoder), 26))
                encoder = '\n'.join(encoder[ i : i + 135 ] for i in range(0, len(encoder), 135))
            with open('encode.txt', 'w', encoding='utf-8') as file:
                file.write(encoder)
            print('{}{}{}{}'.format('\n', Bcolors.B, Bcolors.U, "File successfully encrypted!"))

        except FileNotFoundError:
            print('{}{}{}'.format(Bcolors.R, Bcolors.U, 'File not found!'))