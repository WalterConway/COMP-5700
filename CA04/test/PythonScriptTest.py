import unittest
import CA04.prod.PythonScript as PythonScript
import os

class TestPythonScript(unittest.TestCase):

# Constructor
    #100_0xx ... happy 
    def test100_010_ShouldConstructPythonScriptFullPath(self):
        self.assertIsInstance(PythonScript.PythonScript(fileName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationComments.py"), PythonScript.PythonScript)
    
    def test100_020_ShouldConstructPythonScriptRelativePath(self):
        self.assertIsInstance(PythonScript.PythonScript(fileName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationComments.py"), PythonScript.PythonScript)
            
    #100_9xx ... sad path
    def test100_910_ShouldRaiseExceptionOnNoFilename(self):
        expectedString = "PythonScript.__init__:"
        try:
            myPythonScript = PythonScript.PythonScript()                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))
    
    def test100_920_ShouldRaiseExceptionEmptyFilename(self):
        expectedString = "PythonScript.__init__:"
        try:
            myPythonScript = PythonScript.PythonScript("")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))
    
    def test100_930_ShouldRaiseExceptionOnFilenameOfWrongType(self):
        expectedString = "PythonScript.__init__:"
        try:
            myPythonScript = PythonScript.PythonScript(42)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))
            
    def test100_940_ShouldRaiseExceptionOnNonPythonFilename(self):
        expectedString = "PythonScript.__init__:"
        try:
            myPythonScript = PythonScript.PythonScript("file.java")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))
            
    def test100_950_ShouldRaiseExceptionOnFilenameNotExists(self):
        expectedString = "PythonScript.__init__:"
        try:
            myPythonScript = PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\CA03Validation/validationO.py")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                      
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except AssertionError:
            self.fail("exception was not raised") 
        except Exception as e:
            self.fail("incorrect exception was raised: " + str(e))
    
# getFileName
    #200_0xx ... happy 
    def test200_010_ShouldReturnFilenameFromFilename(self):
        itemToCompare = "PythonScriptTest.py"
        self.assertEquals(itemToCompare, PythonScript.PythonScript("PythonScriptTest.py").getFileName())
        
    def test200_020_ShouldReturnFilenameFromRelativePath(self):
        itemToCompare = "validationComments.py"
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationComments.py").getFileName())
    
    def test200_030_ShouldReturnFilenameFromAbsolutePath(self):
        itemToCompare = "PythonScriptTest.py"
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Development\\Python\\git\\softwareProcess\\wjc0008\\CA03\\test\\PythonScriptTest.py").getFileName())
    
# getFilePath
    #300_0xx ... happy
    def test300_010_ShouldReturnFilepath(self):
        itemToCompare = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation"
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationComments.py").getFilePath())
    
# countLoc
    #400_0xx ... happy
    def test400_010_ShouldReturnLocCountValidationComments(self):
        itemToCompare = 0
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationComments.py").countLoc())
    
    def test400_020_ShouldReturnLocCountValidationDocstrings(self):
        itemToCompare = 15
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationDocstrings.py").countLoc())

    def test400_030_ShouldReturnLocCountValidationFD(self):
        itemToCompare = 9
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationFD.py").countLoc())
    
    def test400_040_ShouldReturnLocCountValidationHybrid(self):
        itemToCompare = 21
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationHybrid.py").countLoc())
    
    def test400_050_ShouldReturnLocCountValidationKeywords(self):
        itemToCompare = 6
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationKeywords.py").countLoc())
    
    def test400_060_ShouldReturnLocCountValidationNoComponents(self):
        itemToCompare = 6
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationNoComponents.py").countLoc())
    
    def test400_070_ShouldReturnLocCountValidationOO(self):
        itemToCompare = 12
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationOO.py").countLoc())
    
    def test400_080_ShouldReturnLocCountValidationRandom(self):
        itemToCompare = 100
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationRandom.py").countLoc())
    
    def test400_090_ShouldReturnLocCountValidationStrings(self):
        itemToCompare = 13
        self.assertEquals(itemToCompare, PythonScript.PythonScript("C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\validationStrings.py").countLoc())

# extractDesign
    #500_0xx ... happy
    def test500_010_ShouldReturnDesignTupleValidationComments(self):
        #=======================================================================
        # Expected Results for validationComments.py
        # No Components
        # Total LOC = 0
        #=======================================================================
        ooList = []
        fdList =[]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationComments.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
        
    def test500_020_ShouldReturnDesignTupleValidationDocstrings(self):
        #=======================================================================
        # Expected Results for validationDocstrings.py
        # Component("docStringFunction1",1,2)
        # Component("docStringFunction2",1,2)
        # Component("docStringFunction3",1,2)
        # Component("DocStringClassA",4,9)
        # Total LOC = 15
        #=======================================================================
        ooList = ["DocStringClassA",4,9]
        fdList =["docStringFunction1",1,2,"docStringFunction2",1,2,"docStringFunction3",1,2]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationDocstrings.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
        
    def test500_030_ShouldReturnDesignTupleValidationFD(self):
        #=======================================================================
        # Expected Results for validationFD.py
        # Component("functionA",1,2)
        # Component("functionB",1,2)
        # Component("functionC",1,2)
        # Component("functionD",1,2)
        # Total LOC = 9
        #=======================================================================
        ooList = []
        fdList =["functionA",1,2,"functionB",1,2,"functionC",1,2,"functionD",1,2]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationFD.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
    
    def test500_040_ShouldReturnDesignTupleValidationHybrid(self):
        #=======================================================================
        # Expected Results for validationHybrid.py
        # Component("HybridClassA",3,7)
        # Component("HybridClassB",0,2)
        # Component("hybridFunctionA",1,2)
        # Component("hybridFunctionB",1,2)
        # Component("hybridFunctionC",1,2)
        # Total LOC = 21
        #=======================================================================
        ooList = ["HybridClassA",3,7,"HybridClassB",0,2]
        fdList =["hybridFunctionA",1,2,"hybridFunctionB",1,2,"hybridFunctionC",1,2]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationHybrid.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
    
    def test500_050_ShouldReturnDesignTupleValidationKeywords(self):
        #=======================================================================
        # Expected Results for validationKeywords.py
        # Component("AClass", 1, 6)
        # Total LOC = 0
        #=======================================================================
        ooList = ["AClass",1,6,]
        fdList =[]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationKeywords.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
    
    def test500_060_ShouldReturnDesignTupleValidationNoComponents(self):
        #=======================================================================
        # Expected Results for validationNoComponents.py
        # No Components
        # Total LOC = 21
        #=======================================================================
        ooList = []
        fdList =[]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationNoComponents.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
    
    def test500_070_ShouldReturnDesignTupleValidationOO(self):
        #=======================================================================
        # Expected Results for validationOO.py
        # Component("ClassA",2,5)
        # Component("ClassB",1,3)
        # Component("ClassC",0,2)
        # Total LOC = 12
        #=======================================================================
        ooList = ["ClassA",2,5,"ClassB",1,3,"ClassC",0,2]
        fdList =[]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationOO.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
    
    def test500_080_ShouldReturnDesignTupleValidationRandom(self):
        #=======================================================================
        # Expected Results for validationRandom.py
        # Component("det",1,24)
        # Component("num",1,7)
        # Component("what",1,26)
        # Component("encrypt",1,17)
        # Component("decrypt",1,19)
        # Total LOC = 100
        #=======================================================================
        ooList = []
        fdList =["decrypt",1,19,"det",1,24,"encrypt",1,17,"num",1,7,"what",1,26]
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationRandom.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)
        

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)
    
    def test500_090_ShouldReturnDesignTupleValidationStrings(self):
        #=======================================================================
        # Expected Results for validationStrings.py
        # Component("EvilStrings", 1, 13)
        # Total LOC = 13
        #=======================================================================
        ooList = ["EvilStrings",1,13]
        fdList = []
        pathName = "C:\\Users\\WalterC\\Desktop\\Software Process\\CA04\\CA03_TestFiles\\CA03Validation\\"
        fileName = "validationStrings.py"
        myScript = PythonScript.PythonScript(os.path.join(pathName, fileName))
#extract the design
        extractedDesign = myScript.extractDesign()

#check for the correct oo information
        ooExtractedDesign = extractedDesign[0]
        ooResultList=[]
        for anOoComponent in ooExtractedDesign:
            ooResultList.append(anOoComponent.getName())
            ooResultList.append(anOoComponent.getMethodCount())
            ooResultList.append(anOoComponent.getLocCount())
        self.assertListEqual(ooList, ooResultList)

#check for the correct fd information
        fdExtractedDesign = extractedDesign[1]
        fdResultList=[]
        for anFdComponent in fdExtractedDesign:
            fdResultList.append(anFdComponent.getName())
            fdResultList.append(anFdComponent.getMethodCount())
            fdResultList.append(anFdComponent.getLocCount())
        self.assertListEqual(fdList, fdResultList)