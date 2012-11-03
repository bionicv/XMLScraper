'''
Created on Nov 2, 2012
@author: Vukosi Marivate
'''
import unittest
from SimpleXMLScrape import RunXMLScrape

class Test(unittest.TestCase):


    def setUp(self):
        self.data = "<test>bomb</test>"
        self.tag = "test"

    def tearDown(self):
        pass


    def testName(self):
        result = RunXMLScrape(self.data, self.tag)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "bomb")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
