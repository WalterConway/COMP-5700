'''
Created on Oct 24, 2014

@author: WalterC
'''
import os
from ..prod import Component
import re
class PythonScript(object):
    
    def __init__(self, fileName=None):
        if(self.isPythonFile(fileName)):
            self.pythonScriptFileName = fileName
        else:
            raise ValueError("PythonScript.__init__:  Not a valid input for fileName")

    def isPythonFile(self, fileName):
        if(fileName is not None):
            if(isinstance(fileName, str)):
                if(len(fileName) != 0):
                    if(fileName.endswith(".py")):
                        tempFileName = os.path.basename(fileName)
                        if(len(tempFileName) >= 4):
                            if(os.path.exists(fileName)):
                                return True
                            else:
                                return False  # file does not exist, or you do not have access to the file.
                        else:
                            return False  # the file must have at least one character.
                    else:
                        return False  # doesn't have the .py at the end
                else:
                    return False  # empty string")
            else:
                return False  # not a instance of string
        else:
            return False  # fileName is required
    
    def getFileName(self):
        return os.path.basename(self.pythonScriptFileName)
    
    def getFilePath(self):
        return os.path.dirname(self.pythonScriptFileName)
    # private method
    def getFileAndPath(self):
        return self.pythonScriptFileName
    
    def countLoc(self):
        mCounter = Counter()
        mPythonFile = PythonFile(self.getFileAndPath())
        mPythonNonCodeAdapter = PythonNonCodeAdapter(mPythonFile)
        while(True):
            line = mPythonNonCodeAdapter.getLineInSequence()
            if(line != None):
                mCounter.incrementCounter()
            else:
                break
        return mCounter.getCurrentCount()
    
    def extractDesign(self):
        mPythonFile = PythonFile(self.getFileAndPath())
        mPythonNonCodeAdapter = PythonNonCodeAdapter(mPythonFile)
        designList = ([], [])
        subDefTokenPattern = re.compile("(?<=^    def )+([\w]+)")
        defTokenPattern = re.compile("(?<=^def )+([\w]+)")
        classTokenPattern = re.compile("(?<=^class )+([\w]+)")
        tabSpaceTokenPattern = re.compile("^(    )")
        pastLine = None
        # obtain all the decomposedMethods
        while(True):
            if(pastLine == None):
                line = mPythonNonCodeAdapter.getLineInSequence()  # get current line and increment to the next line
            else:
                line = pastLine
                pastLine = None
            if(line != None):
                resultDefToken = defTokenPattern.search(line)
                if resultDefToken:  # true if there is a match
                    decomposedMethodCodeList = []
                    decomposedMethodCodeList.append(line)  # add the line to count later
                    decomposedMethodName = resultDefToken.group(0) 
                    while(True):
                        tempLine = mPythonNonCodeAdapter.getLineInSequence()  # get next line since it is in the method
                        if(tempLine != None):
                            resultTabSpaceTokenPattern = tabSpaceTokenPattern.search(tempLine)  # if there is a space in the beginning of the line
                            if resultTabSpaceTokenPattern:
                                decomposedMethodCodeList.append(tempLine)  # this line has a space at the start and therefore must be part of the method
                                continue
                            else:  # found the line that is not part of the method
                                decomposedMethodLoc = len(decomposedMethodCodeList)  # counting the number codes that are part of the method
                                designList[1].append(Component.Component(decomposedMethodName, 1, decomposedMethodLoc))
                                pastLine = tempLine
                                break
                        else:
                            decomposedMethodLoc = len(decomposedMethodCodeList)  # counting the number codes that are part of the method
                            designList[1].append(Component.Component(decomposedMethodName, 1, decomposedMethodLoc))
                            pastLine = tempLine
                            break  # if the file is done with.... no idea what to do right now
                else:
                    continue
            else:
                break  # end of file

        mPythonNonCodeAdapter.resetLineIndex()
        pastLine = None
        
        while(True):
            if(pastLine == None):
                line = mPythonNonCodeAdapter.getLineInSequence()  # get current line and increment to the next line
            else:
                line = pastLine
                pastLine = None
            if(line != None):
                resultClassToken = classTokenPattern.search(line)
                if resultClassToken:
                    composedMethodCodeList = []
                    composedSubDefMethodCodeList = []
                    composedMethodCodeList.append(line)
                    composedMethodName = resultClassToken.group(0)
                    while(True):
                        tempLine = mPythonNonCodeAdapter.getLineInSequence()
                        if(tempLine != None):
                            resultTabSpaceTokenPattern = tabSpaceTokenPattern.search(tempLine)
                            if resultTabSpaceTokenPattern:
                                composedMethodCodeList.append(tempLine)
                                resultSubDefToken = subDefTokenPattern.search(tempLine)
                                if resultSubDefToken:
                                    composedSubDefMethodCodeList.append(tempLine)
                                continue
                            else:
                                composedMethodLoc = len(composedMethodCodeList)
                                composedSubDefMethodCodeListNumber = len(composedSubDefMethodCodeList)
                                designList[0].append(Component.Component(composedMethodName, composedSubDefMethodCodeListNumber, composedMethodLoc))
                                pastLine = tempLine
                                break
                        else:
                                composedMethodLoc = len(composedMethodCodeList)
                                composedSubDefMethodCodeListNumber = len(composedSubDefMethodCodeList)
                                designList[0].append(Component.Component(composedMethodName, composedSubDefMethodCodeListNumber, composedMethodLoc))
                                break
                else:
                    continue
            else:
                break        
        # before returning sort the list by component name
        if(len(designList[0]) != 0):
            sorted(designList[0], key=lambda item:item.getName)
        if(len(designList[1]) != 0):
            sorted(designList[1], key=lambda item:item.getName)
        return designList
    
class Counter(object):

    def __init__(self):
        self.currentCount = 0
    
    def incrementCounter(self):
        self.currentCount = self.currentCount + 1
        
    def getCurrentCount(self):
        return self.currentCount

class Line(object):
    def __init__(self, pythonFileObject):
        self.mPythonFileObject = pythonFileObject
        self.notPartOfMultLineDoc = True
    
    def isEmptyLine(self, LineFromPythonFile):
        tempLine = LineFromPythonFile.strip()
        if(len(tempLine) == 0):
            return True
        return False
    
    def isDocString(self, LineFromPythonFile):
        tempLine = LineFromPythonFile.strip()
        if(not tempLine.endswith("\\")):
            if(self.notPartOfMultLineDoc):
                if(tempLine.startswith("'''")):
                    # Case 1: '''''' or '''blah'''
                    if(len(tempLine) > 3 and tempLine.startswith("'''") and tempLine.endswith("'''")):
                        return True
                    # Case 2: where there is a ''' on any line after the initial token
                    else:
                        while (True):
                            tempLine = self.mPythonFileObject.getLineInSequence()
                            if(tempLine is not None):
                                if(tempLine.find("'''") == -1):
                                    continue
                                else:
                                    return True
                            else:
                                return True
                else:
                    return False
            else:
                self.notPartOfMultLineDoc = True
        else:
            self.notPartOfMultLineDoc = False

    def isComment(self, LineFromPythonFile):
        tempLine = LineFromPythonFile.strip()
        if(tempLine.startswith("#")):
            return True
        return False
    
    def isMultLineComment(self, LineFromPythonFile):        
        tempLine = LineFromPythonFile.strip()
        if(tempLine.startswith('"""')):
            # Case 1: """""" or """blah"""
            if(len(tempLine) > 3 and tempLine.startswith('"""') and tempLine.endswith('"""')):
                return True
            # Case 2: where there is a """ on any line after the initial token
            else:
                while (True):
                    tempLine = self.mPythonFileObject.getLineInSequence()
                    if(tempLine is not None):
                        if(tempLine.find('"""') == -1):
                            continue
                        else:
                            return True
                    else:
                        return True
        else:
            return False
        
class PythonFile(object):
    
    def __init__(self, fileName):
        tempFile = open(fileName)
        self.pythonFileLines = tempFile.readlines()
        tempFile.close()
        self.currentLineNumber = 0
        self.maxLineNumber = len(self.pythonFileLines)
        
    def getCurrentLine(self):
        if(self.maxLineNumber > 0):
            return self.pythonFileLines[self.currentLineNumber]
        else:
            return None
        
    def getLineInSequence(self):
        if(self.currentLineNumber == self.maxLineNumber):
            return None
        else:
            tempLineNumber = self.currentLineNumber
            self.currentLineNumber = self.currentLineNumber + 1
            return self.pythonFileLines[tempLineNumber]
        
    def getNextLine(self):
        if(self.currentLineNumber == self.maxLineNumber):
            return None
        else:
            self.currentLineNumber = self.currentLineNumber + 1
            return self.pythonFileLines[self.currentLineNumber]
    
    def resetLineIndex(self):
        self.currentLineNumber = 0

class PythonNonCodeAdapter(object): 
    
    def __init__(self, pythonFile):
        self.pyFile = pythonFile
        self.pythonLine = Line(self.pyFile)
        self.filteredLines = [] 
        self.currentLineNumber = 0
        self.maxLineNumber = 0
        self.filter()
        
    def filter(self):
        while(True):
            line = self.pyFile.getLineInSequence()
            if(line != None):
                if(self.pythonLine.isEmptyLine(line)):
                    continue
                if(self.pythonLine.isComment(line)):
                    continue
                if(self.pythonLine.isMultLineComment(line)):
                    continue
                if(self.pythonLine.isDocString(line)):
                    continue
                self.filteredLines.append(line)
            else:
                self.maxLineNumber = len(self.filteredLines)
                break
                
    def getCurrentLine(self):
        if(self.maxLineNumber > 0):
            return self.filteredLines[self.currentLineNumber]
        else:
            return None
        
    def getLineInSequence(self):
        if(self.currentLineNumber == self.maxLineNumber):
            return None
        else:
            tempLineNumber = self.currentLineNumber
            self.currentLineNumber = self.currentLineNumber + 1
            return self.filteredLines[tempLineNumber]
                
    def getNextLine(self):
        if(self.currentLineNumber == self.maxLineNumber):
            return None
        else:
            self.currentLineNumber = self.currentLineNumber + 1
            return self.filteredLines[self.currentLineNumber]
        
    def resetLineIndex(self):
        self.currentLineNumber = 0