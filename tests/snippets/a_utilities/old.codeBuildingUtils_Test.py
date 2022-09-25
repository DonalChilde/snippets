"""
Created on Oct 30, 2017

@author: croaker
"""
import unittest

from utilities.codeBuildingUtils.codeBuildingUtils import makeRepr


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_MakeRepr(self):
        class Foo(object):
            def __init__(self, var1=10, var2=20):
                self.var1 = var1
                self.var2 = var2

            def __repr__(self):
                msg = "<Foo(var1 = {}, var2 = {})>"
                attributes = [self.var1, self.var2]
                return msg.format(*attributes)

        foo = Foo()
        makeRepr(Foo, Foo(), None)
        #         MakeRepr.makeRepr()

        print(foo)


#         print(foo.__dict__)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_printRepr']
    unittest.main()
