'''
Created on Nov 1, 2014

@author: WalterC
'''
import unittest
from ..prod import Project
from ..prod import Iteration


class ProjectTest(unittest.TestCase):

    def test_instantiation(self):
        self.assertIsInstance(Project.Project(), Project.Project)
        
    def test_ProjectAddIteration(self):
        testIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        actualResult = myProject.add(testIteration)
        self.assertEquals(actualResult, 1)
        
    def test_ProjectGetIterationCount(self):
        testIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(testIteration)
        actualResult = myProject.getIterationCount()
        self.assertEquals(actualResult, 1)
        
    def test_ProjectGetEffort(self):
        testIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(testIteration)
        actualResult = myProject.getEffort()
        self.assertEquals(actualResult, 30)
        
    def test_ProjectGetPV(self):
        testIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(testIteration)
        actualResult = myProject.getPV()
        self.assertEquals(actualResult, 4)
        
    def test_ProjectGetIteration(self):
        testIteration = Iteration.Iteration(30,4)
        myProject = Project.Project()
        myProject.add(testIteration)
        actualResult = myProject.getIteration(iterationNumber=1)
        self.assertEquals(actualResult, testIteration) #might have to change this.
        
    def test_ProjectGetIterationForInvalidIterationNumberAboveTheCurrentCount(self):
        testIteration = Iteration.Iteration(100,10)
        myProject = Project.Project()
        myProject.add(testIteration)
        expectedString = "Project.getIteration:"
        try:
            myProject.getIteration(iterationNumber=42)                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_ProjectGetIterationForInvalidIterationNumberOfZero(self):
        testIteration = Iteration.Iteration(100,10)
        myProject = Project.Project()
        myProject.add(testIteration)
        expectedString = "Project.getIteration:"
        try:
            myProject.getIteration(iterationNumber=0)                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
            
    def test_ProjectGetIterationForInvalidIterationNumberType(self):
        testIteration = Iteration.Iteration(100,10)
        myProject = Project.Project()
        myProject.add(testIteration)
        expectedString = "Project.getIteration:"
        try:
            myProject.getIteration(iterationNumber="42")                                        
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
    
    def test_ProjectGetEffortForZeroIterations(self):
        myProject = Project.Project()
        actualResult = myProject.getEffort()
        self.assertEquals(actualResult, 0)
        
    def test_ProjectGetPVForZeroIterations(self):
        myProject = Project.Project()
        actualResult = myProject.getPV()
        self.assertEquals(actualResult, 0)
        
    def test_ProejctAddIterationNoParam(self):
        myProject = Project.Project()
        expectedString = "Project.add:"
        try:
            myProject.add()                                      
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 