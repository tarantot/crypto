Program for correspondence encryption

If you want to have encrypted correspondence, then both users need to read the instructions and set the same keys. The keys need to be transferred as privately as possible - it can be a personal meeting, sending using a different encryption method, or some other option.

Obviously, the program is intended to be used primarily on a PC, and not on an Android phone.

Python3 must be installed 

After starting the program - you need to create new keys (it needs to be done only once, but you can change it anytime), to do this, select item 5. The keys will be created and automatically written to the keys.txt file, which will appear in the directory where the program is. The keys must be copied and replaced at the end of the program code.

In the directory with the program, create an empty file main.txt
Now everything is ready for further use. The rest of the options:

1 - encode: keyboard input
Enter text to encrypt using the keyboard. Option for typing small texts. Everything is written in one line, data entry is interrupted by pressing ENTER.

2 - encode: input from a file
Option to encrypt text in main.txt file. First you need to write or copy the desired text into this file and save it. Then select 2, the encode.txt file will be created with the encrypted text in the directory with the program. Please note that the contents of the encode.txt file will be overwritten during the next encryption!

3 - decode: keyboard input
Enter text to decrypt. Just paste the copied ciphertext and press ENTER.

4 - decode: input from a file
Option to decode text in encode.txt file. A decode.txt file will be created with the decoded text. The file is also overwritten the next time it is decrypted.

And exit the program by typing 6.
6 - exit
