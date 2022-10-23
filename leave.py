from __init__ import *

class Leave:
    q = f'\n{Bcolors.B}{Bcolors.U} Completed!'

    def depart(self):
        print(self.q)
        
        return sys.exit()