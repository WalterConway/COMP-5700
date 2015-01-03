'''
Created on Nov 1, 2014

@author: WalterC
'''

class Calendar(object):

    def __init__(self):
        self.dayEffortDict={}
    
    def add(self, day = None, effort = None):
        if(day is not None and effort is not None):
            if(isinstance(day,int) and isinstance(effort,int)):
                if(day > 0 and effort >= 0):
                    self.dayEffortDict[day] = effort
                    return sum(self.dayEffortDict.values())
                else:
                    raise ValueError("Calendar.add:  param is less than what is acceptable")
            else:
                raise ValueError("Calendar.add:  param is not an acceptable type")
        else:
            raise ValueError("Calendar.add:  param is required")
    
    def getLength(self):
        if(len(self.dayEffortDict) == 0):
            return 0
        else:
            tempSortedKeysList = sorted(self.dayEffortDict)
            return tempSortedKeysList[len(tempSortedKeysList)-1]
    
    def get(self, day = None):
        if(day is not None):
            if(isinstance(day, int)):
                if(day > 0):
                    return self.dayEffortDict.get(day,0)
                else:
                    raise ValueError("Calendar.get:  day is less than or equal to zero.")
            else:
                raise ValueError("Calendar.get:  day is not an integer.")
        else:
            raise ValueError("Calendar.get:  day is required a param.")