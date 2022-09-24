"""
Created on Nov 2, 2017

@author: croaker

Useful copy/paste code.


"""
UNIT_TEST_HEADER = """

import unittest
import pprint
import logging
from timeit import default_timer as timer
from utilities.codeBuildingUtils.codeBuildingUtils import print_def__repr__
from utilities.codeBuildingUtils.codeBuildingUtils import prettyPrintData


# setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


"""

MAKE_REPR = '''

def make_repr(self):
        """
        Helper function when calling print_def__repr__
        """
        TEST_THE_INSTANCE = True
        #The class to be tested
        classObj = None


        #UnComment this line to test the class object
        #This sometimes gives a better result
#         TEST_THE_INSTANCE = False

        if TEST_THE_INSTANCE:
            #An instance of the class to be tested
            instance = classObj()
            testClass = instance
        else:
            testClass = classObj

        #pass an edited attribute list if necessary
        attributeList = None
        print_def__repr__(testClass,attributeList)
        print(classObj)
        if TEST_THE_INSTANCE:
            print(instance)
'''
