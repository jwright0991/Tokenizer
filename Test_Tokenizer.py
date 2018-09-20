from Tokenizer import Tokenizer
import unittest

spacers = set(['\n',' ','\t','\r'])
reserved = {'program':1,'begin':2,'end':3,'int':4,'if':5,'then':6,'else':7,'while':8,'loop':9, 'read':10,'write':11,'and':12,'or':13}
specialSymbols = {';':14,',':15,'=':16,'!':17,'[':18,']':19,'(':20,')':21,'+':22, '-':23,'*':24,'!=':25,'==':26,'>=':27,'<=':28, '>':29,'<':30}
intRegEx = r"[1-9][0-9]*|0"
identifierRegEx = r"[A-Z]+[0-9]*"

class Test_Tokenizer(unittest.TestCase):
    
    def test_getStartOfNextToken_3(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "   HELLO, WORLD!"
        expected = 3
        test = tokenizer._Tokenizer__getStartOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)  
    def test_getStartOfNextToken_EqEqEq(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "==="
        expected = 0
        test = tokenizer._Tokenizer__getStartOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_getStartOfNextToken_0(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "HELLO, WORLD!"
        expected = 0
        test = tokenizer._Tokenizer__getStartOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_getStartOfNextToken_Len(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "             "
        expected = len(testStr)
        test = tokenizer._Tokenizer__getStartOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_getStartOfNextToken_1(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = " Hello, World!"
        expected = 1
        test = tokenizer._Tokenizer__getStartOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    
    def test_getEndOfNextToken_3(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "HEL LO, WORLD!"
        expected = 2
        test = tokenizer._Tokenizer__getEndOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_getEndOfNextToken_0(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = " HELLO, WORLD!"
        expected = 0
        test = tokenizer._Tokenizer__getEndOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_getEndOfNextToken_Len(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "HELLO"
        expected = len(testStr)-1
        test = tokenizer._Tokenizer__getEndOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_getEndOfNextToken_1(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "HE "
        expected = 1
        test = tokenizer._Tokenizer__getEndOfNextToken(testStr,0)
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "HELLO, WORLD!"
        expected = ["HELLO", ",", "WORLD", "!"]
        tokenizer._Tokenizer__tokenizeLine(testStr, 1)
        test = tokenizer.tokens[1]
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine_1(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "HELLO"
        expected = ["HELLO"]
        tokenizer._Tokenizer__tokenizeLine(testStr, 1)
        test = tokenizer.tokens[1]
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine_2a(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = " HELLO, WORLD!"
        expected = ["HELLO", ",", "WORLD", "!"]
        tokenizer._Tokenizer__tokenizeLine(testStr,1)
        test = tokenizer.tokens[1]
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine_2b(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = " HELLO, WORLD! "
        expected = ["HELLO",",", "WORLD", "!"]
        tokenizer._Tokenizer__tokenizeLine(testStr,1)
        test = tokenizer.tokens[1]
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine_triple_eq_XY(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "X === Y"
        expected = ["X","==", "=", "Y"]
        tokenizer._Tokenizer__tokenizeLine(testStr,1)
        test = tokenizer.tokens[1]
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine_X_eq_Y_NoSpace(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "X=Y"
        expected = ["X","=", "Y"]
        tokenizer._Tokenizer__tokenizeLine(testStr,1)
        test = tokenizer.tokens[1]
        file.close()
        self.assertEqual(expected,test)
    def test_tokenizeLine_fail(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "XYZa"
        expected = "Error: [Line 1] Invalid ID token 'XYZa'"
        file.close()
        self.assertEqual(expected,tokenizer._Tokenizer__tokenizeLine(testStr,1))
    def test_tokenizeLine_fail_with_reserved(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "XYZend"
        expected = "Error: [Line 1] Invalid ID token 'XYZend'"
        file.close()
        self.assertEqual(expected,tokenizer._Tokenizer__tokenizeLine(testStr,1))
    def test_isAcceptedInteger_true_base(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "123"
        file.close()
        self.assertEqual(True,tokenizer._Tokenizer__isAcceptedInteger(testStr))
    def test_isAcceptedInteger_false_PostA(self):
        fileName = "TestFile_1.CORE"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        testStr = "123A"
        file.close()
        self.assertEqual(False,tokenizer._Tokenizer__isAcceptedInteger(testStr))
    def test_Tokenizer_1(self):
        fileName = "test-pa1/validAllOneLine.core"
        file = open(fileName, "r")
        tokenizer = Tokenizer(file,spacers,reserved,specialSymbols,intRegEx,identifierRegEx)
        tokenizer.tokenize()
        file.close()
        expected_output = [1,4,32,15,32,14,2,32,16,31,14,8,20,32,29,31,21,9,11,32,14,10,32,14,3,14,3,33]
        self.assertEqual(expected_output,tokenizer.tokens_output)
        
if __name__ =='__main__':
    unittest.main()






















