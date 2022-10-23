from __init__ import *

class Key:
    @staticmethod
    def keys():
        mix = [encoder1, encoder2, encoder3, encoder4]
        a = 0
        res = ''
        for b in mix:
            a += 1
            res += '{}{}{}{}{}{}{}'.format("encoder", str(a), " = ", "'''", ''.join(random.sample(b, len(b))), "'''", '\n')
            with open('keys.txt', mode='w', encoding='utf8') as f:
                f.write(res)
        print('{}{}{}{}'.format(Bcolors.B, Bcolors.U, '\n', 'Done! New keys are found in the file keys.txt'))