'''
Created on Sep 12, 2014

@author: Walter Conway
'''

# Component is an abstraction that represents a software component.
# The abstraction models the software component as having a name, number of lines of code, number of methods.
class Component(object):

    # Creates an instance of a Component, saving its name, number of methods, and number of lines of code.                 
    def __init__(self, name=None, methodCount=None, locCount=None):
        if(name is not None):
            if(isinstance(name, str)):
                if(len(name) > 0):
                    self.componentName = name
                else:
                    raise ValueError("Component.__init__:  The name variable is less than zero.")
            else:
                raise ValueError("Component.__init__:  The name variable is not an instance of a string.")
        else:
            raise ValueError("Component.__init__:  The name variable is required")
        
        if(methodCount is not None):
            if(isinstance(methodCount, int)):
                if(methodCount >= 0):
                    self.componentMethodCount = methodCount
                else:
                    raise ValueError("Component.__init__:  The methodCount variable is less than zero.")
            else:
                raise ValueError("Component.__init__:  The methodCount variable is not an instance of a integer.")
        else:
            raise ValueError("Component.__init__:  The methodCount variable is required")
                
        if(locCount is not None):   
            if(isinstance(locCount, int)):
                if(locCount > 0):
                    self.componentLocCount = locCount
                else:
                    raise ValueError("Component.__init__:  The locCount variable is less than or equal to zero.")
            else:
                raise ValueError("Component.__init__:  The locCount variable is not a instance of a integer.")
        else:
            raise ValueError("Component.__init__:  The locCount variable is required")

    # Returns the name of the component.
    def getName(self):
        return self.componentName

    # Returns the component's number of methods.
    def getMethodCount(self):
        return self.componentMethodCount

    # Returns the component's line-of-code count
    def getLocCount(self):
        return self.componentLocCount
    
    def setRelativeSize(self, size="M"):
        if(isinstance(size, str)):
            tempStringOfSize = size.upper()
            if(tempStringOfSize == "VS" or tempStringOfSize == "S" or tempStringOfSize == "M" or tempStringOfSize == "L" or tempStringOfSize == "VL"):
                self.componentSize = tempStringOfSize   
                return self.componentSize
            else:
                raise ValueError("Component.setRelativeSize:  The size variable is not a acceptable input.")
        else:
            raise ValueError("Component.setRelativeSize:  The size variable is not a instance of a string.")
        
    def getRelativeSize(self):
        if(hasattr(self, 'componentSize')):
            return self.componentSize
        else:
            raise ValueError("Component.getRelativeSize:  The size variable has not been set.")
        
