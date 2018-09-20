import re
'''
TOKENIZER_MODEL is (

    file: File object
    tokens: finite set of ordered pairs (integer, string)
    tokens_output: finite set of ordered pairs (integer, integer)
    currentTokenIndex: integer
    spacers: finite set of strings
    reserved: finite set of ordered pairs(string, integer)
    specialSymbols: finite set of ordered pairs(string, integer)
    intRegEx: raw string -> r""
    identifierRegEx: raw string
    )

type Tokenizer is modeled by TOKENIZER_MODEL
'''
class Tokenizer:
    #constructor method
    def __init__(self,file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx):
        self.file = file
        self.tokens = dict()
        self.tokens_output = []
        self.currentTokenIndex = 0
        self.spacers = spacers
        self.reserved = reserved
        self.specialSymbols = specialSymbols
        self.intRegEx = intRegEx
        self.identifierRegEx = identifierRegEx
        self.integer_token = len(reserved) + len(specialSymbols) + 1
        self.identifier_token = len(reserved) + len(specialSymbols) + 2
        self.end_of_file_token = len(reserved) + len(specialSymbols) + 3
    #returns the number of tokens that were produced
    def __len__(self):
        return len(self.tokens_output)
   
    #Returns the value in tokens_output at position currentToken 
    def currentToken(self):
        return str(self.tokens_output[self.currentTokenIndex])
    
    #Increments the token index
    #@requires currentToken < |tokens_output|
    #@ensures self.currentToken = #self.currentToken + 1
    def nextToken(self):
        self.currentTokenIndex += 1

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
        self.tokens_output.append(self.end_of_file_token)
    #Tokenizes a line in a file
    #@param line
    #   The string being tokenized
    #@param lineNumber
    #   The integer index of the line in the file
    #@updates self.tokens_output, self.tokens
    #@Returns None if there was no issue with tokenizing, and an Error message[string] otherwise
    def __tokenizeLine(self, line, lineNumber):
        self.tokens[lineNumber] = []
        start = self.__getStartOfNextToken(line, 0)
        while start < len(line):
            end = self.__getEndOfNextToken(line,start)
            #if the substring(potential token) is not a whitespace character
            if line[start] not in self.spacers:
                tokenNumber = 0
                #check if reserved
                if line[start:end+1] in self.reserved:
                    tokenNumber = self.reserved[line[start:end+1]]
                #check if special symbol
                elif line[start:end+1] in self.specialSymbols:
                    tokenNumber = self.specialSymbols[line[start:end+1]]
                #check if integer
                elif self.__isAcceptedInteger(line[start:end+1]):
                    tokenNumber = self.integer_token
                #check if identifier
                elif self.__isAcceptedIdentifier(line[start:end+1]):
                    tokenNumber = self.identifier_token
                #otherwise an error. Clear and return error message
                else:
                    self.__clear()
                    return"Error: " + "[Line " + str(lineNumber) + "] Invalid ID token '" + str(line[start:end+1]+"'") 
                #add the token to the output list 
                self.tokens_output.append(tokenNumber)
                self.tokens[lineNumber].append(line[start:end+1])
            #increment the start to be the index after the end of the last token and repeat
            start = end+1
    #Checks whether a given token matches the regular expression for an identifier
    #@param token
    #   The token being checked against the RegEx
    #@requires |token| > 0
    #@returns boolean: True if the entire token matches the RegEx, false otherwise
    def __isAcceptedIdentifier(self,token):
        REObj = re.search(self.identifierRegEx, token)
        expected = (0,len(token))
        if REObj == None:
            return False
        return expected == REObj.span()
    #Checks whether a given token matches the regular expression for an integer
    #@param token
    #   The token being checked against the RegEx
    #@requires |token| > 0
    #@returns boolean: True if the entire token matches the RegEx, false otherwise
    def __isAcceptedInteger(self,token):
        REObj = re.search(self.intRegEx, token)
        expected = (0,len(token))
        if REObj == None:
            return False
        return expected == REObj.span()
    
    #Returns the start of a token, given some starting index in a string.
    #@param line
    #   The string which is being tokenized
    #@param start
    #   The integer index of where to start looking for the next token
    #@returns an integer of the index of the first non-separator, at or after the starting index
    #@ensures returned integer index >= start
    def __getStartOfNextToken(self,line,start):
        #if the line starts with a space, keep consuming 
        if line[start] in self.spacers:
            index = start
            while index+1 < len(line) and line[index + 1] in self.spacers:
                index +=1
            return index + 1
        else:
            return start
    #Returns the end of a token, given the starting index of the token
    #@param line
    #   The string which is being tokenized
    #@param start
    #   The integer index of the start of the token
    #@requires line is a string and line[start] != a sepertor
    #@returns an integer index of the last character in the token
    #@ensures returned integer index >= start
    def __getEndOfNextToken(self,line,start):
        if line[start] in self.specialSymbols:
            index = start
            while index+1 < len(line) and line[index + 1] in self.specialSymbols and line[start:index + 2] in self.specialSymbols:
                index +=1
            return index
        elif line[start] not in self.spacers:
            index = start
            while index+1 < len(line) and line[index + 1] not in self.spacers and line[index +1] not in self.specialSymbols:
                index +=1
            return index
        else:
            return start
    
   




        
