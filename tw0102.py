import json
import re
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 轉本調 import 查可能本調
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def main():
    with open('tw0102.json') as trs:
        tsuliau = json.load(trs)
    合音提掉 = re.compile('[(（].+?[)）]')
    數字 = re.compile('\d{2,}')

    kiatko = []
    for tsua in tsuliau:
        han = 合音提掉.sub(' XXX ', tsua[1].replace('_', ' '))
        sooji = 數字.sub(轉漢字, han)
        lo = tsua[2].replace('_', '-')
        pun = []
        臺羅陣列 = []
        tsitpit = {
            '檔名': tsua[0],
            '通用漢羅': tsua[1],
            '原始通用': tsua[2],
            '無合音通用漢羅': han,
            '漢字數字無合音通用漢羅': sooji,
            '連字符通用': lo,
        }
        愛 = True
        臺羅口語 = []
        try:
            for ji in 揣物件(sooji, lo, tsua).篩出字物件():
                if ji.音標敢著(通用拼音音標):
                    tl = ji.轉音(通用拼音音標)
                    臺羅口語.append(tl.音)
                    臺羅 = 查可能本調(tl.型, tl.音)
                    臺羅陣列.append(臺羅)
                    pun.append(臺灣閩南語羅馬字拼音(臺羅).轉通用拼音())
                else:
                    愛 = False
        except 解析錯誤:
            愛 = False
        if 愛:
            tsitpit['臺羅口語'] = '-'.join(臺羅口語)
            tsitpit['通用本調'] = '-'.join(pun)
            tsitpit['台羅本調'] = '-'.join(臺羅陣列)
        kiatko.append(tsitpit)
    with open('tw0102pun-dict.json', 'w') as tong:
        json.dump(
            kiatko, tong,
            ensure_ascii=False, sort_keys=True, indent=2
        )


def 揣物件(han, lo, tsua):
    try:
        return 拆文分析器.建立句物件(han, lo)
    except 解析錯誤:
        print(tsua)
        raise
    return 拆文分析器.建立句物件(lo, lo)


數字對照 = {
    '0': '零',
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九',
}


def 轉漢字(match):
    han = []
    for a in match.group(0):
        han.append(數字對照[a])
    return ''.join(han)


main()
