import unittest
from ..prod import Component

class TestComponent(unittest.TestCase):

# Constructor
    #100_0xx ... happy 
    def test100_010_ShouldConstructComponent(self):
        self.assertIsInstance(Component.Component(name="c1", methodCount=5, locCount=100), Component.Component)
        
        
    #100_9xx ... sad path
    def test100_910_ShouldRaiseExceptionOnNonStringNameConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name=1, methodCount=5, locCount=100)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised") 
    
    def test100_920_ShouldRaiseExceptionOnEmptyStringNameConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="", methodCount=5, locCount=100)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")     

    def test100_930_ShouldRaiseExceptionOnNonIntMethodCountConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="C1", methodCount="a", locCount=100)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")     
    
    def test100_940_ShouldRaiseExceptionOnInvalidMethodCountConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="C1", methodCount=-1, locCount=100)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")     
 
    def test100_950_ShouldRaiseExceptionOnNonIntLocCountConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="C1", methodCount=1, locCount="a")                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")    
    
    def test100_960_ShouldRaiseExceptionOnInvalidLocCountConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="C1", methodCount=1, locCount=0)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")    
            
    def test100_970_ShouldRaiseExceptionOnMissingNameConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(methodCount=1, locCount=0)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")    
            
    def test100_980_ShouldRaiseExceptionOnMissingMethodCountConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="C1", locCount=0)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

    def test100_960_ShouldRaiseExceptionOnMissingLocCountConstructor(self):
        expectedString = "Component.__init__:"
        try:
            myComponent = Component.Component(name="C1", methodCount=1)                                                
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
          
# getName
    #200_0xx ... happy path
    #design decision:
    def test200_010_shouldReturnName(self):
        itemToCompare = "C1"
        self.assertEquals(itemToCompare, Component.Component(itemToCompare, 5, 100).getName())
    
# getMethodCount
    #200_0xx ... happy path
    #design decision:
    def test300_010_shouldReturnMethodCount(self):
        itemToCompare = 1
        self.assertEquals(itemToCompare, Component.Component("C1", itemToCompare, 100).getMethodCount())
              
# getLocCount
    #200_0xx ... happy path
    #design decision:
    def test400_010_shouldReturnLocCount(self):
        itemToCompare = 100
        self.assertEquals(itemToCompare, Component.Component("C1", 0, itemToCompare).getLocCount())
#---------------- CA02 -------------------------        
# setRelativeSize(size)
    def test500_010_shouldSetRelativeSize(self):
        size = "VL"
        theComponent = Component.Component("C1", 5, 100)
        self.assertEquals(size, theComponent.setRelativeSize("VL"))
        
    def test500_020_shouldSetRelativeSizeCaseInsensitive(self):
        size = "Vl"
        theComponent = Component.Component("C1", 5, 100)
        self.assertEquals(size.upper(), theComponent.setRelativeSize("Vl"))
        
    def test500_030_shouldSetDefaultRelativeSize(self):
        size = "M"
        theComponent = Component.Component("C1", 5, 100)
        self.assertEquals(size, theComponent.setRelativeSize())
        
    def test500_910_ShouldObjectToBadSize(self):
        expectedString = "Component.setRelativeSize:"
        try:
            myComponent = Component.Component("CX", 1, 100)   
            myComponent.setRelativeSize("x")                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
            
    def test500_920_ShouldObjectToBadSizeType(self):
        expectedString = "Component.setRelativeSize:"
        try:
            myComponent = Component.Component("CX", 1, 100)   
            myComponent.setRelativeSize(42)                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")

# getRelativeSize()
    def test600_010_ShouldGetRelativeSize(self):
        size = "L"
        theComponent = Component.Component("C1", 5, 100)
        theComponent.setRelativeSize(size)
        self.assertEquals(size, theComponent.getRelativeSize())
        
            
    def test600_920_ShouldObjectToNoSizeSet(self):
        expectedString = "Component.getRelativeSize:"
        try:
            myComponent = Component.Component("CX", 1, 100)   
            myComponent.getRelativeSize()                                             
            self.fail("exception was not raised")                    
        except ValueError as raisedException:                                           
            diagnosticString = raisedException.args[0]                                   
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)]) 
        except:
            self.fail("incorrect exception was raised")
  
if __name__ == '__main__':
    unittest.main()
    
