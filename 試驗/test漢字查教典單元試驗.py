from unittest.case import TestCase
from 轉本調 import 漢字查教典


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(
            set(漢字查教典(self.漢)),
            set(self.辭典)
        )

    def test_管(self):
        self.漢 = '管'
        self.辭典 = ['kng2', 'kuan2', 'kong2']

    def test_𪜶(self):
        self.漢 = '𪜶'
        self.辭典 = ['in1']

    def test_揣無(self):
        self.漢 = 'ㄠ'
        self.辭典 = []
