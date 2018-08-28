import csv
import json
with open('tw0102pun.csv', 'wt', encoding='utf-8') as itaigicsv:

    with open('tw0102pun-dict.json', encoding='utf-8') as f:
        tsuliau = json.load(f)
    fieldnames = [
        '檔名', '通用漢羅', '原始通用',
        '無合音通用漢羅', '連字符通用',
        '通用本調', '台羅本調',
    ]
    itaigi = csv.DictWriter(
        itaigicsv, fieldnames=fieldnames
    )
    itaigi.writeheader()
    for pit in tsuliau:
        itaigi.writerow(pit)
