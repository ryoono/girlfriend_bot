# -*- coding: utf-8 -*-

import random

stampTable = [
   [6325,10979918],
   [6325,10979919],
   [6359,11069851],
   [8515,16581253],
   [8515,16581260],
   [11537,52002742],
   [11537,52002764],
   [11539,52114111],
   [11539,52114112],
   [11539,52114116],
   [11539,52114118],
   [11539,52114121],
   [11539,52114143]
]

# 挨拶メッセージ作成
# ヘッダー/フッターテーブルからランダムに挨拶を作成して返す
def stampMain():
   
   resStampNum = stampTable[random.randint( 0, len(stampTable)-1)]
   return resStampNum

# テスト用
if __name__ == "__main__":

   num = stampMain()
   print( num )
   print( num[0] )
   print( num[1] )