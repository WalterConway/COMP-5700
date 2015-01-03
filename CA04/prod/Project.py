'''
Created on Nov 1, 2014

@author: WalterC
'''

class Project(object):

    def __init__(self):
        self.iterationList = []
    
    def add(self, iteration = None):
        if(iteration is not None):
            self.iterationList.append(iteration)
            return len(self.iterationList)
        else:
            raise ValueError("Project.add:  iteration param is required")
        
    def getIterationCount(self):
        return len(self.iterationList)
    
    def getIteration(self, iterationNumber=None):
        if(iterationNumber is not None):
            if(isinstance(iterationNumber, int)):
                if(iterationNumber > 0):
                    if(iterationNumber <= self.getIterationCount()):
                        return self.iterationList[iterationNumber -1]
                    else:
                        raise ValueError("Project.getIteration:  iteration param is trying to access a invalid iteration.")
                else:
                    raise ValueError("Project.getIteration:  iteration param is less than zero")
            else:
                raise ValueError("Project.getIteration:  iteration param is not an integer")
        else:
            raise ValueError("Project.getIteration:  iteration param is required")
        
    def getEffort(self):
        tempEffortSum =0
        for iterationItem in self.iterationList[:]:
            tempEffortSum = tempEffortSum + iterationItem.getEffort()
        return tempEffortSum
        
    
    def getPV(self):
        tempPVSum =0
        for iterationItem in self.iterationList[:]:
            tempPVSum = tempPVSum + iterationItem.getPV()
        return tempPVSum