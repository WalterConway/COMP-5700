'''
Created on Nov 1, 2014

@author: WalterC
'''

class Iteration(object):

    def __init__(self, effort = None, plannedVelocity = None):
        if(effort is not None and plannedVelocity is not None):
            if(isinstance(effort, int) and isinstance(plannedVelocity, int)):
                if(effort > 0 and plannedVelocity > 0):
                    self.iterationEffort = effort
                    self.plannedVelocity = plannedVelocity
                else:
                    raise ValueError("Iteration.__init__:  effort or plannedVelocity is less than or equal to zero.")
            else:
                raise ValueError("Iteration.__init__:  effort or plannedVelocity is not a integer type.")
        else:
            raise ValueError("Iteration.__init__:  effort or plannedVelocity is required input")
        
    def getEffort(self):
        return self.iterationEffort
    
    def getPV(self):
        return self.plannedVelocity
        