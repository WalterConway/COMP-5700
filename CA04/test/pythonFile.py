'''
Created by Walter
test file for PythonScript 15 LOC 2 Classes

doc string that ends on a single line
'''

'''
doc string that does not end on a single line
if(True):
    pass
#comment inside a doc string
       end'''
       
'''doc comment on one line'''

"""
multi line comment
test
#comment inside a comment
test
"""

"""
standard multi line
"""

'''
doc statement
'''

"""multi line comment on one line"""

"""
multi line comment that does not end on a single line """
# import something comment
import os 
class ClassA(): 
    def __init__(self): 
        pass 
    def methodA(self, parm1=""): 
        doNothingWithIt = '''This is done''' + \
        '''this is the last line''' + \
        '''nope there is one more''' + passItBack("sfsf")
class ClassB(ClassA): 
    def methodB(self): 
        pass 
def Func(): 
        pass
def passItBack(it):
    return it
