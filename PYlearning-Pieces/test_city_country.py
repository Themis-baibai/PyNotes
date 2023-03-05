#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 11:38
# @Author  : name
# @File    : test_city_country.py

import unittest
from city_function import get_formatted_name

class CityTestCase(unittest.TestCase):
    '''测试city_function.py'''
    def test_city_country(self):
        formatted_name=get_formatted_name("beijing","china")
        self.assertEqual(formatted_name,"Beijing,China")

    def test_city_country_populatio(self):
        formatted_name=get_formatted_name('santiago','chile','5000000')
        self.assertEqual(formatted_name,"Santiago,Chile-population 5000000")

if __name__=="__main__":
    unittest.main()


