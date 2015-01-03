'''
Created on Sep 12, 2014

@author: Walter Conway
'''

import math
from ..prod import Component

# The Repository class represents a collection of software components.
class Repository(object):
    
    # Creates an instance of Repository that is capable of holding a specified number of software components.
    # The instance is initially empty.                
    def __init__(self, capacity=100):
        if(isinstance(capacity, int)):
            if(capacity > 0):
                self.capacityValue = capacity
                self.componentList = []
            else:
                raise ValueError("Repository.__init__:  The capacity variable needs to be greater than zero")
        else:
            raise ValueError("Repository.__init__:  The capacity variable is not a instance of a integer.")
        
    
    # Adds an instance of Component to the repository.
    # If adding the component will exceed the repository's capacity,
    # the oldest component in the repostory is removed before the new component is added.
    # addComponent returns the total number of components that are in the repository 
    # (e.g., adding the first component returns 1, adding the second component returns 2,
    # adding the 101st component to a repository with a capacity of 100 returns 100, etc.)
    # addComponent does not check for duplicate components or components with duplicate names.                
    def addComponent(self, component=None):
        if(component is not None):
            componentListAmount = len(self.componentList)
            if(not self.isComponentDuplicate(component)):
                if(componentListAmount < self.capacityValue):
                    self.componentList.append(component)
                elif(componentListAmount == self.capacityValue):
                    self.componentList.pop(0)
                    self.componentList.append(component)
                return len(self.componentList)
            else:
                raise ValueError("Repository.addComponent:  The component is a duplicate")
        else:
            raise ValueError("Repository.addComponent:  The component variable is required.")
    
    def isComponentDuplicate(self, component):
        for tempComponent in self.componentList[:]:
            if((tempComponent is component) or tempComponent.getName() == component.getName()):
                return True
        return False
    
    def isComponentNameDuplicated(self,name):
        for tempComponent in self.componentList[:]:
            if(tempComponent.getName() == name):
                return True
        return False
    
    # Returns a count of the components in the repository. Returns 0 if the repository is empty.
    def count(self):
        return len(self.componentList)
    
    # Returns the number of the components in the repository that have method count .GT. 0.
    def validCount(self):
        methodCountGTZero = 0
        methodCountValue = 0
        for x in range(0, self.count()):
            methodCountValue = self.componentList[x].getMethodCount()
            if(methodCountValue > 0):
                methodCountGTZero = methodCountGTZero + 1
        return methodCountGTZero

    # Returns a list of integers that characterize the lines of code for very small, small, medium, large, and very large components.                
    def determineRelativeSizes(self):
        if(self.validCount() < 2):
            raise ValueError("Repository.determineRelativeSizes:  There are less than two components in the repository that have that have a method count of greater than zero.")
        else:
            normalizedSizeValueList = self.calculateNormalizedSize()
            normalizedAverageValue = self.calculateAverage(normalizedSizeValueList)
            standardDeviation = self.calculateStandardDeviation(normalizedSizeValueList, normalizedAverageValue)
            verySmallMidValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,-2)
            smallMidValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,-1)
            mediumMidValue = self.calculateRelativeSize(normalizedAverageValue,standardDeviation,0)
            largeMidValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,1)
            veryLargeMidValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,2)
            sizeList = [verySmallMidValue, smallMidValue, mediumMidValue, largeMidValue, veryLargeMidValue]
            return sizeList
        
    # Returns a list of normalized size of each component with at least one method
    def calculateNormalizedSize(self):
        normalizedSizeList = []
        for x in range(self.count()):
            tempComponent = self.componentList[x]
            if(tempComponent.getMethodCount() > 0):
                normalizedSizeList.append(math.log(tempComponent.getLocCount() / tempComponent.getMethodCount()))
        return normalizedSizeList
    
    # Calculates the average of the normalized valued list that is passed as a parameter.
    def calculateAverage(self, normalizedSizeList):
        return sum(normalizedSizeList) / len(normalizedSizeList)
    
    # Calculates the standard deviation of the normalized valued list that is passed as well as the normalized average that is also passed as a parameter.
    def calculateStandardDeviation(self, normalizedSizeList, normalizedAverage):
        tempList = []
        for x in range(len(normalizedSizeList)):
            tempList.append(math.pow((normalizedSizeList[x] - normalizedAverage), 2))
        variance = sum(tempList) / (len(tempList) - 1)
        standardDev = math.sqrt(variance)
        return standardDev
    
    # Returns the capacity of the repository
    def getCapacity(self):
        return self.capacityValue
    
    # Calculates relative size to the nearest integer
    # Formula Used: ceiling(e^(Normalized Average+shiftAmount*stdev))
    def calculateRelativeSize(self,normalizedAverage,standardDeviation,shiftAmount):
        return int(math.ceil(math.exp(normalizedAverage + (shiftAmount * standardDeviation))))
    
    def getRelativeSize(self,component=None):
        if(component is not None):
            if(self.validCount() < 2):
                raise ValueError("Repository.getRelativeSize:  There are less than two components in the repository that have that have a method count of greater than zero.")
            else:
                if(component.getMethodCount() > 0):
                    inputSize = component.getLocCount()/component.getMethodCount()
                    normalizedSizeValueList = self.calculateNormalizedSize()
                    normalizedAverageValue = self.calculateAverage(normalizedSizeValueList)
                    standardDeviation = self.calculateStandardDeviation(normalizedSizeValueList, normalizedAverageValue)
                    verySmallHighValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,-1.5)
                    smallHighValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,-0.5)
                    mediumHighValue = self.calculateRelativeSize(normalizedAverageValue,standardDeviation,0.5)
                    largeHighValue = self.calculateRelativeSize(normalizedAverageValue, standardDeviation,1.5)
                    
                    if(inputSize < verySmallHighValue):
                        return "VS"
                    elif(inputSize < smallHighValue):
                        return "S"
                    elif(inputSize < mediumHighValue):
                        return "M"
                    elif(inputSize < largeHighValue):
                        return "L"
                    else:
                        return "VL"
                else:
                    raise ValueError("Repository.getRelativeSize:  The component has zero methods")
        else:
            raise ValueError("Repository.getRelativeSize:  The component variable is required.")

            
    def estimateByRelativeSize(self, name = None, methodCount = None, size = "M"):
        if(self.validCount() >=2):
            if(methodCount != None):
                if(isinstance(methodCount,int)):
                    if(methodCount > 0):
                        if(name != None):
                            if(isinstance(name,str)):
                                if(len(name) > 0):
                                    if(not self.isComponentNameDuplicated(name)):
                                        if(isinstance(size,str)):
                                            relativeSizeList = self.determineRelativeSizes()
                                            upperCaseSize = size.upper()
                                            if(upperCaseSize == "VS"):
                                                linesOfCode = relativeSizeList[0]*methodCount
                                                return Component.Component(name,methodCount,linesOfCode)
                                            elif(upperCaseSize =="S"):
                                                linesOfCode = relativeSizeList[1]*methodCount
                                                return Component.Component(name,methodCount,linesOfCode)
                                            elif(upperCaseSize =="M"):
                                                linesOfCode = relativeSizeList[2]*methodCount
                                                return Component.Component(name,methodCount,linesOfCode)
                                            elif(upperCaseSize =="L"):
                                                linesOfCode = relativeSizeList[3]*methodCount
                                                return Component.Component(name,methodCount,linesOfCode)
                                            elif(upperCaseSize =="VL"):
                                                linesOfCode = relativeSizeList[4]*methodCount
                                                return Component.Component(name,methodCount,linesOfCode)
                                            else:
                                                raise ValueError("Repository.estimateByRelativeSize:  The size variable is not acceptable.")
                                        else:
                                            raise ValueError("Repository.estimateByRelativeSize:  The size variable is not a instance of a string.")
                                    else:
                                        raise ValueError("Repository.estimateByRelativeSize:  The name variable is already in use.")
                                else:
                                    raise ValueError("Repository.estimateByRelativeSize:  The name variable is not long enough.")
                            else:
                                raise ValueError("Repository.estimateByRelativeSize:  The name variable is not a instance of a string.")
                        else:
                            raise ValueError("Repository.estimateByRelativeSize:  The name variable is required.")
                    else:
                        raise ValueError("Repository.estimateByRelativeSize:  The methodCount variable is less than or equal to zero.")
                else:
                    raise ValueError("Repository.estimateByRelativeSize:  The methodCount variable is not a instance of a integer.")
            else:
                raise ValueError("Repository.estimateByRelativeSize:  The methodCount variable is required.")
        else:
            raise ValueError("Repository.estimateByRelativeSize:  There are less than two components in the repository that have that have a method count of greater than zero.")