# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:20:36 2019

@author: amand
"""

import unittest
from funcs import *

class TestPhonebook(unittest.TestCase):
    def test_get_db(self):
        self.assertTrue(check_db("phonebook.db"))
        self.assertIsNotNone(get_db())
        
if __name__ == ("__main__"):
    unittest.main()