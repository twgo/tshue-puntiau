from unittest.case import TestCase
from 轉本調 import 比對揣出本調


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(
            比對揣出本調(self.口, self.辭典),
            self.本
        )

    def test_本調(self):
        self.口 = 'kuan1'
        self.辭典 = ['kuan1']
        self.本 = 'kuan1'

    def test_口語調(self):
        self.口 = 'kuan7'
        self.辭典 = ['kuan1']
        self.本 = 'kuan1'

    def test_h(self):
        self.口 = 'pa2'
        self.辭典 = ['pah4', 'pik']
        self.本 = 'pah4'

    def test_揣無就照口語調(self):
        self.口 = 'tsang9'
        self.辭典 = []
        self.本 = 'tsang9'

    def test_音節仝款就照辭典(self):
        self.口 = 'am9'
        self.辭典 = ['am3']
        self.本 = 'am3'

    def test_差傷濟就照口語調(self):
        self.口 = 'tsang9'
        self.辭典 = ['ing9']
        self.本 = 'tsang9'

    def test_士(self):
        self.口 = 'suh8'
        self.辭典 = ['su7']
        self.本 = 'suh8'

    def test_鄉內埔腔本調(self):
        self.口 = 'hiang1'
        self.辭典 = ['hiong1']
        self.本 = 'hiang1'

    def test_鄉內埔腔變調(self):
        self.口 = 'hiang7'
        self.辭典 = ['hiong1']
        self.本 = 'hiang1'

    def test口語調毋是羅馬字(self):
        self.口 = ','
        self.辭典 = ['，']
        self.本 = '，'

    def test口語調毋是羅馬字辭典無(self):
        self.口 = ','
        self.辭典 = []
        self.本 = ','

    def test_10調(self):
        self.口 = 'neh10'
        self.辭典 = ['ni1', 'ni5', 'neh4', 'ne1', ]
        self.本 = 'neh4'

    def test_10調入聲(self):
        self.口 = 'neh10'
        self.辭典 = ['ni1', 'ni5', 'ne1', ]
        self.本 = 'ne1'

    def test_注入聲(self):
        self.口 = 'khah10'
        self.辭典 = ['kan1',]
        self.本 = 'kan1'
