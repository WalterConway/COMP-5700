'''
Created on Sep 12, 2014

@author: Walter Conway
'''

import math

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
            if(componentListAmount < self.capacityValue):
                self.componentList.append(component)
            elif(componentListAmount == self.capacityValue):
                self.componentList.pop()
                self.componentList.append(component)
            return len(self.componentList)
        else:
            raise ValueError("Repository.addComponent:  The component variable is required.")
    
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
            verySmallValue = self.calculateVerySmall(normalizedAverageValue, standardDeviation)
            smallValue = self.calculateSmall(normalizedAverageValue, standardDeviation)
            mediumValue = self.calculateMedium(normalizedAverageValue, standardDeviation)
            largeValue = self.calculateLarge(normalizedAverageValue, standardDeviation)
            veryLargeValue = self.calculateVeryLarge(normalizedAverageValue, standardDeviation)
            sizeList = [verySmallValue, smallValue, mediumValue, largeValue, veryLargeValue]
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
    
    # Calculates the very small size
    def calculateVerySmall(self, normalizedAverage, standardDeviation):
        return int(math.ceil(math.exp(normalizedAverage - (2 * standardDeviation))))
    
    # Calculates the small size
    def calculateSmall(self, normalizedAverage, standardDeviation):
        return int(math.ceil(math.exp(normalizedAverage - standardDeviation)))
    
    # Calculates the medium size
    def calculateMedium(self, normalizedAverage, standardDeviation):
        return int(math.ceil(math.exp(normalizedAverage)))
    
    # Calculates the large size
    def calculateLarge(self, normalizedAverage, standardDeviation):
        return int(math.ceil(math.exp(normalizedAverage + standardDeviation)))
    
    # Calculates the very large size
    def calculateVeryLarge(self, normalizedAverage, standardDeviation):
        return int(math.ceil(math.exp(normalizedAverage + (2 * standardDeviation))))
