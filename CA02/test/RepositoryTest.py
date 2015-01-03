'''
Created on Sep 12, 2014

@author: Walter Conway
'''
import unittest
from ..prod import Repository
from ..prod import Component


class RepositoryTest(unittest.TestCase):
    
    # Setting up a repository and a component for each test
    def setUp(self):
        self.repository = Repository.Repository(6)
        self.component = Component.Component("C1", 1, 76)
        self.component2 = Component.Component("C2", 4, 116)
        self.component3 = Component.Component("C3", 7, 113)
        self.component4 = Component.Component("C4", 5, 103)
        self.component5 = Component.Component("C5", 0, 10)
    # setting the setup items to None
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.repository = None
        self.component = None
        self.component2 = None
        self.component3 = None
        self.component4 = None
        self.component5 = None
        
    # Testing to see if the component was added to the repository
    # CA01-2.1, Happy
    def test_instantiation(self):
        self.repository = Repository.Repository(2)
        self.assertIsInstance(self.repository, Repository.Repository)
        
    # Testing to see if the capacity of the repository is defaulted to 100
    # CA01-2.1, Happy
    def test_capacity_defaultValue(self):
        self.newRepository = Repository.Repository()
        capacityValue = self.newRepository.getCapacity()
        self.assertEqual(capacityValue, 100)
        
    # Testing to see if the component was added to the repository
    def test_addComponent(self):
        numberOfComponents = self.repository.addComponent(self.component)
        self.assertEqual(numberOfComponents, 1)
    

    # Testing to see if the component was added to the repository
    def test_count(self):
        self.repository.addComponent(self.component)       
        numberOfComponents = self.repository.count()
        self.assertEqual(numberOfComponents, 1)
    

    # Testing to see if the repository counted the component that was added as having more than 0 methods
    # CA01-2.3, Happy
    def test_vaildCount(self):
        self.repository.addComponent(self.component)
        numberOfComponents = self.repository.validCount()
        self.assertEqual(numberOfComponents, 1)
    
    # Testing to see if the repository counted the component that was added as having more than 0 methods
    # `CA01-2.3
    def test_vaildCount_For_Zero_Components(self):
        numberOfComponents = self.repository.validCount()
        self.assertEqual(numberOfComponents, 0)

    # Testing to see if the list that returns with vs,s,m,l,vl are correct
    def test_determineRelativesSizes(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.listValues = self.repository.determineRelativeSizes()
        self.assertAlmostEqual(self.listValues[0], 8)
        self.assertAlmostEqual(self.listValues[1], 15)
        self.assertAlmostEqual(self.listValues[2], 29)
        self.assertAlmostEqual(self.listValues[3], 58)
        self.assertAlmostEqual(self.listValues[4], 115)

    # Testing to see if the normalizedSize Calculation is correctly
    def test_normalizedSize(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        self.assertAlmostEqual(normalizedSizeValueList[0], 4.33073334)
        self.assertAlmostEqual(normalizedSizeValueList[1], 3.36729583)
        self.assertAlmostEqual(normalizedSizeValueList[2], 2.772588722239781)
        self.assertAlmostEqual(normalizedSizeValueList[3], 2.995732273553991)

    # Testing to see if the average is calculated correctly
    def test_avg(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        expectedValue = 3.3665875415166444
        self.assertAlmostEqual(averageValue, expectedValue)
        
    # Testing to see if the standard deviation is calculated correctly
    def test_standardDeviation(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        standardDevValue = self.repository.calculateStandardDeviation(normalizedSizeValueList, averageValue)
        expectedValue = 0.6879791300215806
        self.assertAlmostEqual(standardDevValue, expectedValue)
    

    # Testing to see if the very small value is calculated correctly
    def test_verySmall(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        standardDevValue = self.repository.calculateStandardDeviation(normalizedSizeValueList, averageValue)
        verySmallValue = self.repository.calculateRelativeSize(averageValue, standardDevValue,-2)
        self.assertEqual(verySmallValue, 8)
        
    # Testing to see if the small value is calculated correctly
    def test_small(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        standardDevValue = self.repository.calculateStandardDeviation(normalizedSizeValueList, averageValue)
        smallValue = self.repository.calculateRelativeSize(averageValue, standardDevValue,-1)
        self.assertEqual(smallValue, 15)
    
    # Testing to see if the medium value is calculated correctly
    def test_medium(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        standardDevValue = self.repository.calculateStandardDeviation(normalizedSizeValueList, averageValue)
        mediumValue = self.repository.calculateRelativeSize(averageValue, standardDevValue,0)
        self.assertAlmostEqual(mediumValue, 29)
    
    # Testing to see if the large value is calculated correctly
    def test_large(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        standardDevValue = self.repository.calculateStandardDeviation(normalizedSizeValueList, averageValue)
        largeValue = self.repository.calculateRelativeSize(averageValue, standardDevValue,1)
        self.assertAlmostEqual(largeValue, 58)
        
    # Testing to see if the very large value is calculated correctly
    def test_veryLarge(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        normalizedSizeValueList = self.repository.calculateNormalizedSize()
        averageValue = self.repository.calculateAverage(normalizedSizeValueList)
        standardDevValue = self.repository.calculateStandardDeviation(normalizedSizeValueList, averageValue)
        veryLargeValue = self.repository.calculateRelativeSize(averageValue, standardDevValue,2)
        self.assertAlmostEqual(veryLargeValue, 115)
        

    # Testing to see if the capacity raises a ValueError if there is instance of something besides an integer.
    # CA01-2.1
    def test_capacity_ValueError_For_Instance(self):
        expectedString = "Repository.__init__:"
        try:
            newRepository = Repository.Repository("Failure")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    # Testing to see if the capacity raises a ValueError if there is instance of something besides an integer.
    # CA01-2.1, Sad
    def test_capacity_ValueError_For_LE_Zero(self):
        expectedString = "Repository.__init__:"
        try:
            newRepository = Repository.Repository(0)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")      

    # Testing to see if the capacity of the repository is still 
    # currently at the maximum if by addition to the repository exceeds the maximum capacity.
    def test_capacityValue_overFlow(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.component6 = Component.Component("C6", 11, 250)
        self.component7 = Component.Component("C7", 4, 50)
        self.repository.addComponent(Component.Component("C8", 1, 50))
        numberOfComponents = self.repository.addComponent(Component.Component("C9", 3, 60))
        self.assertIs(numberOfComponents, 6)
        
    # Testing to see if the repository will return zero if it is empty
    def test_Repository_Empty_Return(self):
        self.assertIs(self.repository.count(), 0)
        
    def test_determineRelativeSizes_ValueError_For_LT_Two(self):
        expectedString = "Repository.determineRelativeSizes:"
        newRepository = Repository.Repository()
        self.repository.addComponent(self.component)
        try:
            newRepository.determineRelativeSizes()
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    def test_addComponent_ValueError_For_Duplicate_Component_Instance(self):
        self.repository.addComponent(self.component)
        expectedString = "Repository.addComponent:"
        try:
            self.repository.addComponent(self.component)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_addComponent_ValueError_For_Duplicate_Component_Name(self):
        self.repository.addComponent(self.component)
        expectedString = "Repository.addComponent:"
        newComponent = Component.Component("C1", 2, 5)
        try:
            self.repository.addComponent(newComponent)
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_getRelativeSize_For_VerySmall(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        newComponent = Component.Component("C1", 4, 20)
        self.assertEqual("VS", self.repository.getRelativeSize(newComponent))
        
    def test_getRelativeSize_For_Small(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        newComponent = Component.Component("C1", 1, 15)
        self.assertEqual("S", self.repository.getRelativeSize(newComponent))
        
    def test_getRelativeSize_For_Medium(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        newComponent = Component.Component("C1", 1, 30)
        self.assertEqual("M", self.repository.getRelativeSize(newComponent))
    
    def test_getRelativeSize_For_Large(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        newComponent = Component.Component("C1", 1, 76)
        self.assertEqual("L", self.repository.getRelativeSize(newComponent))
        
    def test_getRelativeSize_For_VeryLarge(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        newComponent = Component.Component("C1", 1, 200)
        self.assertEqual("VL", self.repository.getRelativeSize(newComponent))
        
    def test_getRelativeSize_ValueError_For_No_Parameters(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        expectedString = "Repository.getRelativeSize:"
        try:
            self.repository.getRelativeSize()
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    
    def test_getRelativeSize_ValueError_For_Zero_MethodCount(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)        
        expectedString = "Repository.getRelativeSize:"
        try:
            self.repository.getRelativeSize(Component.Component("C1", 0, 56))
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
        
    def test_getRelativeSize_ValueError_For_Insufficent_Data(self):
        self.repository.addComponent(self.component)      
        expectedString = "Repository.getRelativeSize:"
        try:
            self.repository.getRelativeSize(Component.Component("C9", 1, 90))
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

    def test_estimateByRelativeSize_VerySmall(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.assertEqual(16, self.repository.estimateByRelativeSize("C1",2,"VS").getLocCount())
        
    def test_estimateByRelativeSize_Small(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.assertEqual(30, self.repository.estimateByRelativeSize("C1",2,"S").getLocCount())
    def test_estimateByRelativeSize_Medium(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.assertEqual(58, self.repository.estimateByRelativeSize("C1",2,"M").getLocCount())
    def test_estimateByRelativeSize_Large(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.assertEqual(116, self.repository.estimateByRelativeSize("C1",2,"L").getLocCount())
    def test_estimateByRelativeSize_VeryLarge(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        self.assertEqual(230, self.repository.estimateByRelativeSize("C1",2,"VL").getLocCount())
    def test_estimateByRelativeSize_ValueError_For_Missing_Name(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize(2,"VL")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    def test_estimateByRelativeSize_ValueError_For_Name_LE_Zero(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize("",2,"VL")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_estimateByRelativeSize_ValueError_For_Name_Not_Instance_Of_String(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize(78,2,"VL")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    def test_estimateByRelativeSize_ValueError_For_MethodCount_LE_Zero(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize("C1",0,"L")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    def test_estimateByRelativeSize_ValueError_For_Missing_MethodCount(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize(name="C1",size="L")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
    def test_estimateByRelativeSize_ValueError_For_MethodCount_Not_Instance_Of_Integer(self):
        self.repository.addComponent(self.component)
        self.repository.addComponent(self.component2)
        self.repository.addComponent(self.component3)
        self.repository.addComponent(self.component4)
        self.repository.addComponent(self.component5)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize("C1","2","L")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
            
    def test_estimateByRelativeSize_ValueError_For_Insufficient_Components_In_Repository(self):
        self.repository.addComponent(self.component)
        expectedString = "Repository.estimateByRelativeSize:"
        try:
            self.repository.estimateByRelativeSize("C1",2,"L")
            self.fail("exception was not raised")
        except ValueError as ve:
            diagnosticString = ve.args[0]
            self.assertEqual(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")
        