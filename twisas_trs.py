import json
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 轉本調 import 查可能本調
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


def main():
    with open('twisas-HL-kaldi.json') as trs:
        tsuliau = json.load(trs)

    def 揣物件(han, lo):
        try:
            return 拆文分析器.建立句物件(han, lo)
        except 解析錯誤:
            print(tsua)
            pass
        return 拆文分析器.建立句物件(lo, lo)

    for tsua in tsuliau:
        han = tsua['無合音漢字']
        lo = tsua['口語臺羅']
        句物件 = 揣物件(han, lo)
        for ji in 句物件.篩出字物件():
            ji.音 = 查可能本調(ji.型, ji.音)
        tsua['本調臺羅'] = 句物件.看音()

    with open('twisas-HL-kaldi-pun.json', 'w') as tong:
        json.dump(
            tsuliau, tong,
            ensure_ascii=False, sort_keys=True, indent=2
        )


main()
