import re
'''
TOKENIZER_MODEL is (

    file: two-dimensional array of strings
    isTokenized: boolean,
    tokens: finite set of ordered pairs (integer, string)
    tokens_output: finite set of ordered pairs (integer, integer)
    currentToken: integer
    spacers: finite set of strings
    reserved: finite set of ordered pairs(string, integer)
    specialSymbols: finite set of ordered pairs(string, integer)
    intRegEx: raw string
    identifierRegEx: raw string
    )

type Tokenizer is modeled by TOKENIZER_MODEL
'''
class Tokenizer:
    
    def __init__(self,file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx):
        self.file = file
        self.isTokenized = False
        self.tokens = dict()
        self.tokens_output = []
        self.currentToken = 0
        self.spacers = spacers
        self.reserved = reserved
        self.specialSymbols = specialSymbols
        self.intRegEx = intRegEx
        self.identifierRegEx = identifierRegEx
        

    #Returns the value in tokens_output at position currentToken 
    def currentToken(self):
        return str(tokens_output[self.currentToken])
    
    #Increments the token index
    #@requires currentToken < |tokens_output|
    #@ensures self.currentToken = #self.currentToken + 1
    def nextToken(self):
        self.currentToken += 1

    #Clears the tokenized entries in tokens and tokens_output
    def __clear(self):
        self.tokens = dict()
        self.tokens_output = []
    #Tokenizes self.file
    #@requires self.file is open
    #@returns None if successful or a String with an error message if failed
    def tokenize(self):
        lineNum = 1
        #tokenize each line of the file or return an error message
        for line in self.file:
            error = self.__tokenizeLine(line, lineNum)
            if error:
                return error
            lineNum += 1
        self.tokens[lineNum] = ["__EOF__"]
        self.tokens_output.append(33)
            
    def __tokenizeLine(self, line, lineNumber):
        self.tokens[lineNumber] = []
        start = self.__getStartOfNextToken(line, 0)
        while start < len(line):
            end = self.__getEndOfNextToken(line,start)
            if line[start] not in self.spacers:
                tokenNumber = 0
                if line[start:end+1] in self.reserved:
                    tokenNumber = self.reserved[line[start:end+1]]  
                elif line[start:end+1] in self.specialSymbols:
                    tokenNumber = self.specialSymbols[line[start:end+1]]
                elif self.__isAcceptedInteger(line[start:end+1]):
                    tokenNumber = 31
                elif self.__isAcceptedIdentifier(line[start:end+1]):
                    tokenNumber = 32
                else:
                    self.__clear()
                    return"Error: " + "[Line " + str(lineNumber) + "] Invalid ID token '" + str(line[start:end+1]+"'") 
                self.tokens_output.append(tokenNumber)
                self.tokens[lineNumber].append(line[start:end+1])
            start = end+1
    def __isAcceptedIdentifier(self,token):
        REObj = re.search(self.identifierRegEx, token)
        expected = (0,len(token))
        if REObj == None:
            return False
        return expected == REObj.span()
    def __isAcceptedInteger(self,token):
        REObj = re.search(self.intRegEx, token)
        expected = (0,len(token))
        if REObj == None:
            return False
        return expected == REObj.span()
    def __getStartOfNextToken(self,line,start):
        #if the line starts with a space, keep consuming 
        if line[start] in self.spacers:
            index = start
            while index+1 < len(line) and line[index + 1] in self.spacers:
                index +=1
            return index + 1
        else:
            return start
            
    def __getEndOfNextToken(self,line,start):
        if line[start] in self.specialSymbols:
            index = start
            while index+1 < len(line) and line[index + 1] in self.specialSymbols and (index+1 - start) < 2:
                index +=1
            return index
        elif line[start] not in self.spacers:
            index = start
            while index+1 < len(line) and line[index + 1] not in self.spacers and line[index +1] not in self.specialSymbols:
                index +=1
            return index
        else:
            return start
    
   




        
