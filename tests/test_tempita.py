import os
import unittest
import doctest


class TestTempita(unittest.TestCase):
    def test_readme(self):
        doctest.testfile('../README.rst')

    def test_templating(self):
        doctest.testfile('tests.txt')
