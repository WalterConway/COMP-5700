'''
Created on Nov 1, 2014

@author: WalterC
'''
import unittest
from ..prod import Schedule
from ..prod import Calendar
from ..prod import Project
from ..prod import Iteration


class ScheduleTest(unittest.TestCase):
    
    def test_instantiation(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        self.assertIsInstance(Schedule.Schedule(project=myProject, calendar=myCal), Schedule.Schedule)
        
    def test_GetLastDay(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        actualValue = mySched.getLastDay()
        self.assertEquals(actualValue, 5)
        
    def test_getBurnDownDay(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        actualValue = mySched.getBurnDown(day=3)
        self.assertEquals(actualValue, 50)
        
    def test_getBurnDownDayWithNegativeDay(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        actualValue = mySched.getBurnDown(day=-1)
        self.assertEquals(actualValue, 90)
        
    def test_getPV(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        actualValue = mySched.getPV(day=3)
        self.assertEquals(actualValue, 3)
        
    def test_getPVForCummulatiePVBeforeProjBegins(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        actualValue = mySched.getPV(day=0)
        self.assertEquals(actualValue, 4)
        
    def test_InstanceWithAmountOfTimeIsLessThanTheAmountOfPlannedTime(self):
        expectedString = "Schedule.__init__:"
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        try:
            mySched = Schedule.Schedule(project=myProject, calendar=myCal)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
        
    def test_InstanceWithAmountOfTimeIsLessThanTheAmountOfPlannedTimeWithCalendarEmpty(self):
        expectedString = "Schedule.__init__:"
        myCal = Calendar.Calendar()
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        try:
            mySched = Schedule.Schedule(project=myProject, calendar=myCal)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_InstanceWithAmountOfTimeIsLessThanTheAmountOfPlannedTimeWithProjectEmpty(self):
        expectedString = "Schedule.__init__:"
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myProject = Project.Project()
        try:
            mySched = Schedule.Schedule(project=myProject, calendar=myCal)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_GetPVWithInvalidType(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        expectedString = "Schedule.getPV:"
        try:
            mySched.getPV(day="a")                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
                
    def test_GetPVWithMissingParam(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        expectedString = "Schedule.getPV:"
        try:
            mySched.getPV()                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_GetBurnDownWithMissingParam(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        expectedString = "Schedule.getBurnDown:"
        try:
            mySched.getBurnDown()                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_GetBurnDownWithInvalidType(self):
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        mySched = Schedule.Schedule(project=myProject, calendar=myCal)
        expectedString = "Schedule.getBurnDown:"
        try:
            mySched.getBurnDown(day="a")                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 

    def test_instanceWithInvalidTypeOFProject(self):
        expectedString = "Schedule.__init__:"
        myCal = Calendar.Calendar()
        myCal.add(1,10)
        myCal.add(3,30)
        myCal.add(4,30)
        myCal.add(5,60)
        myCal.add(6,90)
        try:
            mySched = Schedule.Schedule(project="myProject", calendar=myCal)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_instanceWithInvalidTypeOfCalendar(self):
        expectedString = "Schedule.__init__:"
        myProject = Project.Project()
        myProject.add(Iteration.Iteration(30,1))
        myProject.add(Iteration.Iteration(60,3))
        try:
            mySched = Schedule.Schedule(project=myProject, calendar="myCal")                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 