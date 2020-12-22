import unittest
from generator.generator_md import *
class GeneratorTest(unittest.TestCase):
    def test_title(self):
        in_txt = read_all_lines_from('source_leetcode_data.txt')
        text = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
        res = text.get_md_title()
        self.assertEqual(res, '## Merge Intervals\n')

    def test_leetcode_link(self):
        in_txt = read_all_lines_from('source_leetcode_data.txt')
        text = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
        res = text.get_md_solution_link()
        self.assertEqual(res, '+ [Merge Intervals](#merge-intervals)')

    def test_solution(self):
        in_txt = read_all_lines_from('source_leetcode_data.txt')
        text = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
        res = text.get_md_formatted_solution()
        self.assertEqual(res,'## Merge Intervals\n\n+ [Merge Intervals](#merge-intervals)\n\nhttps://leetcode.com/problems/merge-intervals/\n\n``` python\ndef merge(self, intervals: List[List[int]]) -> List[List[int]]:\n    intervals = sorted(intervals, key = lambda x: x[0])\n```\n')