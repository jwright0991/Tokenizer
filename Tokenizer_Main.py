import sys
from Tokenizer import Tokenizer

#Main 
def main(arg1):
    #setting up constants
    spacers = set(['\n',' ','\t','\r'])
    reserved = {'program':1,'begin':2,'end':3,'int':4,'if':5,'then':6,'else':7,'while':8,'loop':9, 'read':10,'write':11,'and':12,'or':13}
    specialSymbols = {';':14,',':15,'=':16,'!':17,'[':18,']':19,'(':20,')':21,'+':22, '-':23,'*':24,'!=':25,'==':26,'>=':27,'<=':28, '>':29,'<':30}
    intRegEx = r"[1-9][0-9]*|0"
    identifierRegEx = r"[A-Z]+[0-9]*"
    file = None
    #Try to open the file and read from it
    try:
        file = open(arg1, "r")
    except FileNotFoundError:
        print("Error: File in Does Not Exist!")
        return  
    #instanciate the tokenizer object
    tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
    #tokenize the file and store the return value into a variable
    error = tokenizer.tokenize()
    #check if tokenizing returned an error and report & return if it did
    if error:
        print(x)
        return
    #print the output tokens
    while tokenizer.currentTokenIndex < len(tokenizer):
        print(tokenizer.currentToken())
        tokenizer.nextToken()
    #close the file
    file.close()
if __name__ == '__main__':
    '''Check to make sure that only two commandline arguments were passed in.'''
    if(len(sys.argv) == 2):
        main(sys.argv[1])
    else:
       print("Error: incorrect number of arguments")
