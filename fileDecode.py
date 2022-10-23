from __init__ import *


class FileDecode:
    @staticmethod
    def file_dec():
        try:
            with open('encode.txt', 'r', encoding='utf-8') as f:
                new_data = f.read().replace("\r", "")
                f.seek(0, os.SEEK_END)  # go to the end of the file
                if f.tell():  # if True
                    f.seek(0)  # go to the beginning to continue usage
                else:
                    f.close()  # close file
                    print('{}{}{}'.format(Bcolors.R, Bcolors.U, 'File is empty!'))
                    return Options.choice()
                new_data = ''.join(new_data[i:i+135] for i in range(0, len(new_data), 136))
                new_data = ''.join(new_data[i:i+26] for i in range(0, len(new_data), 27))
                new_data = ''.join(new_data[i:i+3] for i in range(0, len(new_data), 4))
                i = 1
                decoder = ''
                for x in new_data:
                    if x == '南':
                        decoder += '\n'
                        i += 1
                    elif x == '林':
                        decoder += '\t'
                        i += 1
                    elif len(set(x + encoder2)) != 171:
                        print('{}{}{}{}'.format(Bcolors.R, 'No characters found in the key! ', 'Missing character: ', x))
                        return Options.choice()
                    else:
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

            with open('decode.txt', 'w', encoding='utf-8') as file:
                file.writelines(decoder)
            print('{}{}{}{}'.format('\n', Bcolors.B, Bcolors.U, "File successfully decrypted!"))

        except FileNotFoundError:
            print('{}{}{}'.format(Bcolors.R, Bcolors.U, 'File not found!'))