from unittest import TestCase, main

from whiteboard import solution


class MatchTestCase_Twosum(TestCase):
    def test_example_one(self):
        self.assertEqual(solution([15,7,11,2],9),[1,3])
    def test_example_two(self):
        self.assertEqual(solution([2,3,4],6),[0,2])
    def test_neg(self):
        self.assertEqual(solution([-1,0], -1),[0,1])
    def test_multiple(self):
        self.assertEqual(solution([0,0,1,2,2,5],8), [-1,-1])
    def test_empty(self):
        self.assertEqual(solution([],0),[-1,-1])

if __name__ == '__main__':
    main()