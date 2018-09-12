from unittest.case import TestCase, skip
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

    @skip
    def test_呢(self):
        self.漢 = '呢'
        self.辭典 = ['ni1', 'ni5', 'neh4', 'ne1', ]
