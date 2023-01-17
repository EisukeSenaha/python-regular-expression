import re
"""
match() 文字列の先頭で正規表現とマッチするか判定
search() 文字列を操作して正規表現がどこにマッチするか調べる
findall() 正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditer() 重複しないマッチオブジェクトのイテレータを返す
"""

# 両端がaかcであれば matchオブジェクトを返す
# <re.Match object; span=(0, 3), match='abc'>
# <re.Match object; span=(0, 3), match='axc'>
# axc
m = re.match('a.c', 'abc')
print(m)
m = re.match('a.c', 'axc')
print(m)
print(m.group())

