from __init__ import *


class Options:
    @staticmethod
    def choice():
        while True:
            select = input('Select action:\n')
            if select == "1":
                Encoder.enc()
                print(guide.info())
            elif select == "2":
                FileEncode.file_enc()
                print(guide.info())
            elif select == "3":
                Decoder.dec()
                print(guide.info())
            elif select == "4":
                FileDecode.file_dec()
                print(guide.info())
            elif select == "5":
                Key.keys()
                print(guide.info())
            elif select == "6":
                leave.depart()
                break
            else:
                print('{}{}'.format(Bcolors.R, "Enter 1,2,3,4,5 or 6!"))