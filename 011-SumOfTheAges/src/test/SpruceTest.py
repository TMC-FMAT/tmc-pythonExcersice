# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sys
from io import StringIO
#from tmc import points
from src.Spruce import spruce

@points('1.0')
class  HelloWorldTestCase(unittest.TestCase):
	__qualname__="HelloWorldTest"

	def test_helloWorld(self):
		awaitedValue="Hello World!\n"
		capturedOutput=StringIO.StringIO()
		sys.stdout=capturedOutput
		spruce()
		sys.stdout=sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(),awaitedValue,msg="you need print \"Hello World!\"")
		
if __name__ == '__main__':
	unittest.main()
