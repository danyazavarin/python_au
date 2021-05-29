import unittest
from main import *


class TestGr(unittest.TestCase):
    def test_from_str_to_dict(self):
        lst = ['date, resource, count, staff_id\n', '2020-01, 2, 10, 4\n', '2020-01, 1, 10, 2\n', '2020-02, 4, 20, 4\n', '2020-09, 1, 44, 1\n', '2020-10, 3, 34, 3\n']
        result = from_str_to_dict(lst)
        expect = [{'date': '2020-01', 'resource': '2', 'count': '10', 'staff_id': '4'}, {'date': '2020-01', 'resource': '1', 'count': '10', 'staff_id': '2'}, {'date': '2020-02', 'resource': '4', 'count': '20', 'staff_id': '4'}, {'date': '2020-09', 'resource': '1', 'count': '44', 'staff_id': '1'}, {'date': '2020-10', 'resource': '3', 'count': '34', 'staff_id': '3'}]
        self.assertEqual(expect, result)

    def test_filtrate(self):
        lst = [{'date': '2020-03', 'resource': '1', 'count': '48', 'staff_id': '4'}, {'date': '2020-05', 'resource': '3', 'count': '25', 'staff_id': '4'}, {'date': '2020-01', 'resource': '2', 'count': '10', 'staff_id': '3'}, {'date': '2020-02', 'resource': '2', 'count': '20', 'staff_id': '1'}, {'date': '2020-03', 'resource': '2', 'count': '40', 'staff_id': '1'}, {'date': '2020-04', 'resource': '1', 'count': '48', 'staff_id': '4'}, {'date': '2020-02', 'resource': '1', 'count': '33', 'staff_id': '4'}, {'date': '2020-01', 'resource': '3', 'count': '10', 'staff_id': '2'}, {'date': '2020-04', 'resource': '3', 'count': '23', 'staff_id': '1'}, {'date': '2020-02', 'resource': '3', 'count': '15', 'staff_id': '3'}, {'date': '2020-03', 'resource': '3', 'count': '20', 'staff_id': '2'}, {'date': '2020-05', 'resource': '2', 'count': '16', 'staff_id': '3'}, {'date': '2020-01', 'resource': '1', 'count': '10', 'staff_id': '4'}, {'date': '2020-05', 'resource': '1', 'count': '33', 'staff_id': '2'}, {'date': '2020-04', 'resource': '2', 'count': '80', 'staff_id': '2'}]
        result = filtrate('staff_id', 1, lst)
        expect = [{'date': '2020-02', 'resource': '2', 'count': '20', 'staff_id': '1'}, {'date': '2020-03', 'resource': '2', 'count': '40', 'staff_id': '1'}, {'date': '2020-04', 'resource': '3', 'count': '23', 'staff_id': '1'}]
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
