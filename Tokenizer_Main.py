import sys
from Tokenizer import Tokenizer


def main(arg1):
    spacers = set(['\n',' ','\t','\r'])
    reserved = {'program':1,'begin':2,'end':3,'int':4,'if':5,'then':6,'else':7,'while':8,'loop':9, 'read':10,'write':11,'and':12,'or':13}
    specialSymbols = {';':14,',':15,'=':16,'!':17,'[':18,']':19,'(':20,')':21,'+':22, '-':23,'*':24,'!=':25,'==':26,'>=':27,'<=':28, '>':29,'<':30}
    intRegEx = r"[1-9][0-9]*|0"
    identifierRegEx = r"[A-Z]+[0-9]*"
    try:
        file = open(arg1, "r")
    except FileNotFoundError:
        print("Error: File Does Not Exist!")
        return
    
    tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
    x = tokenizer.tokenize()
    if x != None:
        print(x)
        return
    print(tokenizer.tokens)
    print(tokenizer.tokens_output)
if __name__ == '__main__':
    '''Check to make sure that only two commandline arguments were passed in.'''
    if(len(sys.argv) == 2):
        main(sys.argv[1])
    else:
       print("Error: incorrect number of arguments")
