# Tokenizer

#Tokenizer for the CORE language written in python3

The Tokenizer class is passed a language's keywords, special characters,,seperators, a RegEx for identifiers, a RegEx for integers, and a file to be tokenizer. This is
not CORE language dependent. tokenizer_main.py passes in CORE specific
requirements and Tokenizes a file passed in through commandline arguments.

To run the program, simple run the following in the commandline(within the same directory as the file):

>>python3 Tokenizer_Main.py <file> 

ex: 

>>python3 Tokenizer_Main.py TestFile_1.CORE

a .core extension is not required, but files that do not adhear the the grammar of the CORE language will likely produce errors.

No make file is required since the Tokenizer_Main.py imports the tokenizer class, but Tokenizer_Main.py, Tokenizer.py, and the file you wish to tokenize must be in the same directory.

I provided 20 unit test cases in Test_Tokenizer.py for testing of the Tokenizer class. This file can be run by entering the following command on the commandline(within the same directory as the file):

>>python3 Test_Tokenizer.py

The CORE grammar can be found in CORE.pdf

