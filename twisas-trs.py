import json
import re
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 轉本調 import 查可能本調
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


with open('twisas-HL-kaldi.json') as trs:
    tsuliau = json.load(trs)
合音提掉 = re.compile('\(.+?\)')


def 揣物件(han, lo):
    try:
        return 拆文分析器.建立句物件(han, lo)
    except 解析錯誤:
        print(tsua)
        pass
    return 拆文分析器.建立句物件(lo, lo)


# kiatko = []
for tsua in tsuliau:
    han = tsua['漢字']
    lo = tsua['口語臺羅']
    pun = []
    for ji in 揣物件(han, lo).篩出字物件():
        print((ji.型, ji.音))
        pun.append(查可能本調(ji.型, ji.音))
    tsua['本調臺羅'] = ' '.join(pun)
#     kiatko.append()
with open('twisas-HL-kaldi-pun.json', 'w') as tong:
    json.dump(
        tsuliau, tong,
        ensure_ascii=False, sort_keys=True, indent=2
    )
