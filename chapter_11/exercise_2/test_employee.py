''' Страница упражнения - 216 '''

# 11-3
import unittest

from employee import *

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Di', 'Chi', 100)

    def test_give_default_raise(self):
        raisee = self.employee.give_raise()
        self.assertEqual(raisee, 100 + 5000)

    def test_give_custom_raise(self):
        raisee = self.employee.give_raise(6000)
        self.assertEqual(raisee, 100 + 6000)