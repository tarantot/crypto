from __init__ import *

class Stamp:
    stamp = '{}{}'.format(Bcolors.G, '''\
//----------------------------------------------------------------//
//                _                                               //
//        _      | |                                       __     //
//    ___(_)_ __ | |__   ___ _ __    _ __  _ __  ___     /[__]\   //
//   / __| | '_ \| '_ \ / _ \ '__|  | '_ \  '__|/ _ \   |      |  //
//  | (__| | |_) | | | |  __/ |     | |_) | |  | |_| |  |  ()  |  //
//   \___|_| .__/|_| |_|\___|_|     | .__/|_|   \___/    \____/   //
//         |_|                      |_|                           //
//                                                                //
//  1000111 1101111 100001     version 1.0     Coded by tarantot  //
//----------------------------------------------------------------//''')
    guide = '{}{}{}{}{}{}'.format(
        Bcolors.G, '+-----------------------------+', Bcolors.Y, '''\
  
1 - encode: keyboard input 
2 - encode: input from a file
3 - decode: keyboard input
4 - decode: input from a file
5 - create new keys
6 - exit\n''', 

        Bcolors.G, '+-----------------------------+')

    def label(self):
        return self.stamp

    def info(self):
        return self.guide