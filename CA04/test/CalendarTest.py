'''
Created on Nov 1, 2014

@author: WalterC
'''
import unittest
from ..prod import Calendar

class CalendarTest(unittest.TestCase):
    def test_instantiation(self):
        self.assertIsInstance(Calendar.Calendar(), Calendar.Calendar)

    def test_AddToCalendar(self):
        myCal = Calendar.Calendar()
        actualValue = myCal.add(1,60)
        self.assertEquals(actualValue, 60)
    
    def test_AddTwoDaysToCalendar(self):
        myCal = Calendar.Calendar()
        myCal.add(1,60)
        actualValue = myCal.add(5,120)
        self.assertEquals(actualValue, 180)
        
    def test_AddInvalidDayParamOfZero(self):
        expectedString = "Calendar.add:"
        myCal = Calendar.Calendar()    
        try:
            myCal.add(day=0, effort=60)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 

    def test_AddNoDayParam(self):
        expectedString = "Calendar.add:"
        myCal = Calendar.Calendar()    
        try:
            myCal.add(effort=60)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test_AddInvalidDayParamType(self):
        expectedString = "Calendar.add:"
        myCal = Calendar.Calendar()    
        try:
            myCal.add(day="1", effort=60)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test_AddInvalidEffortParamLessThanZero(self):
        expectedString = "Calendar.add:"
        myCal = Calendar.Calendar()    
        try:
            myCal.add(day=1, effort=-1)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
        
    def test_AddInvalidEffortParamType(self):
        expectedString = "Calendar.add:"
        myCal = Calendar.Calendar()    
        try:
            myCal.add(day=1, effort="60")
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test_AddInvalidEffortParamMissing(self):
        expectedString = "Calendar.add:"
        myCal = Calendar.Calendar()    
        try:
            myCal.add(day=1)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test_GetZerothDay(self):
        expectedString = "Calendar.get:"
        myCal = Calendar.Calendar()
        myCal.add(1,60)    
        try:
            myCal.get(0)
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test_GetLength(self):
        myCal = Calendar.Calendar()
        myCal.add(1,60)
        myCal.add(5,120)
        actualResult = myCal.getLength()
        self.assertEquals(actualResult, 5)
        
    def test_Get(self):
        myCal = Calendar.Calendar()
        myCal.add(1,60)
        myCal.add(5,120)
        actualResult = myCal.get(day=1)
        self.assertEquals(actualResult, 60)
    
    def test_GetInterveningDay(self):
        myCal = Calendar.Calendar()
        myCal.add(1,60)
        myCal.add(5,120)
        actualResult = myCal.get(day=4)
        self.assertEquals(actualResult, 0)