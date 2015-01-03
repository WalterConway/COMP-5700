'''
Created on Nov 1, 2014

@author: WalterC
'''
import unittest
from ..prod import Iteration

class IterationTest(unittest.TestCase):
    def test_instantiation(self):
        self.assertIsInstance(Iteration.Iteration(effort = 120, plannedVelocity=3), Iteration.Iteration)

    def test_InvalidTypeOfEffort(self):
        expectedString = "Iteration.__init__:"
        try:
            testIteration = Iteration.Iteration(effort="120", plannedVelocity=3)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_InvalidTypeOfPlannedVelocity(self):
        expectedString = "Iteration.__init__:"
        try:
            testIteration = Iteration.Iteration(effort=120, plannedVelocity="3")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_NotPassingAEffort(self):
        expectedString = "Iteration.__init__:"
        try:
            testIteration = Iteration.Iteration(plannedVelocity=3)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_notPassingAPlannedVelocity(self):
        expectedString = "Iteration.__init__:"
        try:
            testIteration = Iteration.Iteration(effort=120)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test_getPlannedVelocity(self):
        testIteration = Iteration.Iteration(effort=120, plannedVelocity=3) 
        self.assertEquals(testIteration.getPV(), 3)
        
    def test_getEffort(self):
        testIteration = Iteration.Iteration(effort=120, plannedVelocity=3) 
        self.assertEquals(testIteration.getEffort(), 120)
        
    
    def test_EffortPassingLessThanOrEqualToZero(self):
        expectedString = "Iteration.__init__:"
        try:
            testIteration = Iteration.Iteration(effort=0, plannedVelocity=3)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

    def test_PlannedVelocityPassingLessThanOrEqualToZero(self):
        expectedString = "Iteration.__init__:"
        try:
            testIteration = Iteration.Iteration(effort=120, plannedVelocity=0)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 