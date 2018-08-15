from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


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
