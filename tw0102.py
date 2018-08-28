import json
import re
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 轉本調 import 查可能本調
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


with open('tw0102.json') as trs:
    tsuliau = json.load(trs)
合音提掉 = re.compile('\(.+?\)')


def 揣物件(han, lo):
    try:
        return 拆文分析器.建立句物件(han, lo)
    except 解析錯誤:
        print(tsua)
        raise
    return 拆文分析器.建立句物件(lo, lo)


kiatko = []
for tsua in tsuliau:
    han = 合音提掉.sub(' XXX ', tsua[1].replace('_', ' '))
    lo = tsua[2].replace('_', '-')
    pun = []
    臺羅陣列 = []
    tsitpit = {
        '檔名': tsua[0],
        '通用漢羅': tsua[1],
        '原始通用': tsua[2],
        '無合音通用漢羅': han,
        '連字符通用': lo,
    }
    愛 = True
    try:
        for ji in 揣物件(han, lo).篩出字物件():
            if ji.音標敢著(通用拼音音標):
                tl = ji.轉音(通用拼音音標)
                臺羅 = 查可能本調(tl.型, tl.音)
                臺羅陣列.append(臺羅)
                pun.append(臺灣閩南語羅馬字拼音(臺羅).轉通用拼音())
            else:
                pun.append(ji.音)
                愛 = False
    except 解析錯誤:
        愛 = False
    if 愛:
        tsitpit['通用本調'] = '-'.join(pun)
        tsitpit['台羅本調'] = '-'.join(臺羅陣列)
    kiatko.append(tsitpit)
with open('tw0102pun-dict.json', 'w') as tong:
    json.dump(
        kiatko, tong,
        ensure_ascii=False, sort_keys=True, indent=2
    )
