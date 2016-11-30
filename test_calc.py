# coding: utf-8
from unittest import TestCase
import calc

class TestCalc(TestCase):

	def test_add_one(self):
		self.assertEqual(calc.add_one(1),2)

	def test_add_two(self):
		self.assertEqual(calc.add_one(1),3)

	def test_add_three(self):
		self.assertEqual(calc.add_one(1),4)