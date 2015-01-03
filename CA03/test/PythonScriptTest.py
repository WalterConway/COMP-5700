'''
Created on Oct 24, 2014

@author: WalterC
'''
import unittest
from ..prod import PythonScript

class PythonScriptTest(unittest.TestCase):

    def test_instantiation(self):
        self.assertIsInstance(PythonScript.PythonScript(fileName="pythonFile.py"), PythonScript.PythonScript)
        
    def test_PythonScriptValueErrorForFileNameParamNotPassed(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript()
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_PythonScriptValueErrorForIncorrectType(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript(fileName=45)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    def test_PythonScriptValueErrorForFileExtensionMissing(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript(fileName="pythonFile")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    def test_PythonScriptValueErrorForEmptyString(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript(fileName="")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    def test_PythonScriptValueErrorForFileNameLessThanFourCharacters(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript(".py")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_PythonScriptValueErrorForNotBeingAPythonFile(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript("pythonFile.java")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_PythonScriptValueErrorForFileNotExisting(self):
        expectedString = "PythonScript.__init__:"
        try:
            pyScript = PythonScript.PythonScript("filedoesnotexist.py")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_ServiceMethodGetFileName(self):
        pyScript = PythonScript.PythonScript("pythonFile.py")
        actualString = pyScript.getFileName()
        self.assertEqual(actualString, "pythonFile.py")
    
    def test_ServiceMethodGetFilePath(self):
        pyScript = PythonScript.PythonScript("C:\Users\WalterC\Desktop\Software Process\CA03\pythonFile.py")
        expectedString = pyScript.getFilePath()
        self.assertEqual(expectedString, "C:\Users\WalterC\Desktop\Software Process\CA03")
        
    def test_InnateMethodCountLocForZeroLinesOfCode(self):
        pyScript = PythonScript.PythonScript("blank.py")
        actualString = pyScript.countLoc()
        self.assertEqual(actualString, 0)
        
    def test_InnateMethodCountLoc(self):
        pyScript = PythonScript.PythonScript("pythonFile.py")
        actualString = pyScript.countLoc()
        self.assertEqual(actualString, 15)
        
    def test_InnateMethodExtractDesign(self):
        pyScript = PythonScript.PythonScript("pythonFile.py")
        componentLists = pyScript.extractDesign()
        self.assertEquals("ClassA", componentLists[0][0].getName())
        self.assertEquals("ClassB", componentLists[0][1].getName())
        self.assertEquals("Func", componentLists[1][0].getName())
        
    def test_InnateMethodExtractDesignZeroComponents(self):
        pyScript = PythonScript.PythonScript("pythonFile2.py")
        componentLists = pyScript.extractDesign()
        self.assertEquals(0, len(componentLists[0]))
        self.assertEquals("Func", componentLists[1][0].getName())
        
    def test_InnateMethodExtractDesignZeroDecomposedComponents(self):
        pyScript = PythonScript.PythonScript("pythonFile3.py")
        componentLists = pyScript.extractDesign()
        self.assertEquals(0, len(componentLists[1]))
        self.assertEquals("ClassA", componentLists[0][0].getName())
        self.assertEquals("ClassB", componentLists[0][1].getName())