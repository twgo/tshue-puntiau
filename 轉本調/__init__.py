from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字.models import 用字表

_教典 = {}
for _分詞 in 用字表.全部分詞():
    字物件 = 拆文分析器.分詞字物件(_分詞)
    if not 字物件.音.startswith('0'):
        try:
            _教典[字物件.型].append(字物件.音)
        except KeyError:
            _教典[字物件.型] = [字物件.音]


def 漢字查教典(漢):
    try:
        return sorted(_教典[漢])
    except KeyError:
        return []


def 比對揣出本調(口, 辭典):
    khau = 臺灣閩南語羅馬字拼音(口)
    for su in 辭典:
        pun = 臺灣閩南語羅馬字拼音(su)
        if pun.聲 == khau.聲 and pun.韻 == khau.韻:
            return su
        if pun.聲 == khau.聲 and pun.韻.rstrip('h') == khau.韻:
            return su
    try:
        return khau.聲 + khau.韻 + pun.調
    except UnboundLocalError:
        return 口
