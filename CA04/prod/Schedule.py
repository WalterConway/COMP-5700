'''
Created on Nov 1, 2014

@author: WalterC
'''
from ..prod import Calendar
from ..prod import Project

class Schedule(object):

    def __init__(self, project = None, calendar = None):
        if(project is not None and calendar is not None):
            if(isinstance(project,Project.Project) and isinstance(calendar, Calendar.Calendar)):
                maxEffortInCalendar = self.maxAvaliableEffortInCalendar(calendar)
                projectEffort = project.getEffort()
                if(projectEffort<= maxEffortInCalendar):
                    if(projectEffort > 0 and maxEffortInCalendar > 0):
                        self.scheduleCalendar = calendar
                        self.scheduleProject = project
                    else:
                        raise ValueError("Schedule.__init__: Calendar or Project does not have any days or iterations to start a schedule.")
                else:
                    raise ValueError("Schedule.__init__: Calendar does not have sufficient time to fit project")
            else:
                raise ValueError("Schedule.__init__:  param is not a valid type.")
        else:
            raise ValueError("Schedule.__init__: param is required.")
    
    def maxAvaliableEffortInCalendar(self, calendar):
        lengthOfCalendar = calendar.getLength()
        tempSumOfEffortInCalendar = 0
        if(lengthOfCalendar != 0):
            for day in range(1,lengthOfCalendar+1):
                tempSumOfEffortInCalendar = tempSumOfEffortInCalendar + calendar.get(day)
        return tempSumOfEffortInCalendar
        
    def getLastDay(self):
        lengthOfCalendar = self.scheduleCalendar.getLength()
        effortBurnDown = self.scheduleProject.getEffort()
        for day in range(1,lengthOfCalendar+1):
            effortBurnDown = effortBurnDown - self.scheduleCalendar.get(day)
            if(effortBurnDown <=0):
                return day
    
    def getBurnDown(self, day = None):
        if(day is not None):
            if(isinstance(day, int)):
                if(day > 0):
                    effortBurnDown = self.scheduleProject.getEffort()
                    for dayInCalendar in range(1,day+1):
                        effortBurnDown = effortBurnDown - self.scheduleCalendar.get(dayInCalendar)
                    if(effortBurnDown <=0):
                        return 0
                    else:
                        return effortBurnDown
                else:
                    return self.scheduleProject.getEffort()
            else:
                raise ValueError("Schedule.getBurnDown:  day is not an integer.")
        else:
            raise ValueError("Schedule.getBurnDown: day param is required.")
    
    def getFirstAvaliableDayInCalendar(self):
        totalDays = self.scheduleCalendar.getLength()
        for day in range(1,totalDays +1):
            if(self.scheduleCalendar.get(day)>0):
                return day
            
    
    def getPV(self, day = None):
        if(day is not None):
            if(isinstance(day, int)):
                firstAvaliableDay = self.getFirstAvaliableDayInCalendar()
                if(day < firstAvaliableDay):
                    return self.scheduleProject.getPV()
                else:
                    totalPV = self.scheduleProject.getPV()
                    iteration = 1
                    effortGain = 0
                    for currentDay in range(1,day+1):
                        avaliableEffortForDay = self.scheduleCalendar.get(currentDay)
                        if(effortGain >= 0):
                            projectEffort = self.scheduleProject.getIteration(iteration).getEffort()
                        else:
                            projectEffort = 0
                        effortGain = (avaliableEffortForDay + effortGain) - projectEffort
                        if(effortGain >=0):
                            totalPV = totalPV - self.scheduleProject.getIteration(iteration).getPV()
                            if(totalPV ==0):
                                return totalPV
                            iteration = iteration +1
                    return totalPV
            else:
                raise ValueError("Schedule.getPV:  day is not a integer")
        else:
            raise ValueError("Schedule.getPV:  day is required")
               
                    
    
        