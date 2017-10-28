# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest


class  SanboxTestCase(unittest.TestCase):
    

    def test_sanbox(self):
        self.assertTrue(True)
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()

