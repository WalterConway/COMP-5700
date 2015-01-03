'''
Created on Sep 12, 2014

@author: Walter Conway
'''
import unittest
from ..prod import Component

class ComponentTest(unittest.TestCase):

    # Instantiates a component before each run of a test.
    # CA01-1.1, Happy
    def setUp(self):
        self.component = Component.Component('C1', 4, 20)

    # Checks to see if the return of getName is in fact C1.
    # CA01-1.2, Happy
    def test_GetName(self):
        self.assertIs(self.component.getName(), "C1")

    # Checks if the method count of C1 is 4
    # CA01-1.3, Happy
    def test_GetMethodCount(self):
        self.assertIs(self.component.getMethodCount(), 4)

    # Checks if the number of lines of code in C1 is 20
    # CA01-1.4, Happy
    def test_GetLocCount(self):
        self.assertIs(self.component.getLocCount(), 20)

    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_Name_ValueError_For_None(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component(methodCount=4, locCount=20)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_Name_ValueError_For_LE_Zero(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component("", 4, 20)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
        
    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_Name_ValueError_For_Not_Instance(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component(3, 4, 20)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_MethodCount_ValueError_For_None(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component(name="C1", locCount=20)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
        
    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_MethodCount_ValueErrorFor_LT_Zero(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component("C1", -1, 20)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_MethodCount_ValueError_For_Not_Instance(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component("C1", "Failure", 20)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_locCount_ValueError_For_None(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component(name="C1", methodCount=4)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
        
    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_locCount_ValueError_For_LE_Zero(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component("C1", 4, 0)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

    # Checks the Error message to ensure that the ValueError message is raised and caught with the intended Error Message
    # CA01-1.1, Sad
    def test_locCount_ValueError_For_Not_Instance(self):
        expectedString = "Component.__init__:"
        try:
            self.newComponent = Component.Component("C1", 4, "Failure")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
