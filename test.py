# -*- coding:utf-8 -*-
import unittest
import tmp
"""
"""



"""
class testFunc(unittest.TestCase):


"""

class testFunc(unittest.TestCase):
  def test_one(self):
    c = tmp.Calc()
    self.assertEqual("anokutara", c.ichi() )
  
  def test_red(self):
    d = tmp.Calc()
    self.assertEqual(12, d.king() )
  
  def test_three(self):
    f = tmp.fzbz()
    self.assertEqual(1 , f.shi(1) )
  
  def test_four(self):
    f = tmp.fzbz()
    self.assertEqual(2 , f.shi(2) )


"""
# ユニットテスト
class testFunc(unittest.TestCase):
  def setup(self):
    self.seq = range(10)
  
  def test_aaaa(self):
    self.assertTrue(True)

  def test_aaab(self):
    self.assertTrue(True)
"""


if __name__ == '__main__':
  unittest.main()

