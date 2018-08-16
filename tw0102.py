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
        pass
    return 拆文分析器.建立句物件(lo, lo)


kiatko = []
for tsua in tsuliau:
    han = 合音提掉.sub(' XXX ', tsua[1])
    lo = tsua[2].replace('_', ' ')
    pun = []
    for ji in 揣物件(han, lo).篩出字物件():
        if ji.音標敢著(通用拼音音標):
            tl = ji.轉音(通用拼音音標)
            臺羅 = 查可能本調(tl.型, tl.音)
            pun.append(臺灣閩南語羅馬字拼音(臺羅).轉通用拼音())
        else:
            pun.append(ji.音)
    kiatko.append(tsua + ['-'.join(pun)])
with open('tw0102pun.json', 'w') as tong:
    json.dump(
        kiatko, tong,
        ensure_ascii=False, sort_keys=True, indent=2
    )
