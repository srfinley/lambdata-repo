"""Testing file for lambdata functionality"""

import unittest
import lambdata_srfinley as lds
from lambdata_srfinley import df_utils as dfu


class BaseTests(unittest.TestCase):
    """test functions in __init__"""
    def test_increment(self):
        self.assertEqual(lds.increment(10), 11)


class DFUTests(unittest.TestCase):
    """test objects and functions in df_utils"""
    def test_wrappedDF_height(self):
        wrapped = dfu.WrappedDF(dfu.DATES)
        self.assertEqual(wrapped.get_height(), 4)

    def test_wrappedDF_width(self):
        wrapped = dfu.WrappedDF(dfu.DATES)
        self.assertEqual(wrapped.get_width(), 1)

    def test_wrappedDF_break(self):
        wrapped = dfu.WrappedDF(dfu.DATES)
        wrapped.df = dfu.break_date(wrapped.df, 'dates')
        self.assertEqual(wrapped.get_width(), 4)

    def test_add_column(self):
        df = dfu.add_column(dfu.DATES, [1, 2, 3, 4], "newcol")
        wrapped = dfu.WrappedDF(df)
        self.assertEqual(wrapped.get_width(), 2)

if __name__ == '__main__':
    unittest.main()
