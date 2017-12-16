# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest


class SandboxTestCase(unittest.TestCase):

    def test_sandbox(self):
        self.assertTrue(True)
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()

