# -*- coding: utf-8 -*-

import random

import greeting
import stamp
import weatherForecast

# スタンプメッセージ発生割合( 0% ~ 100% )
STAMP_OCCURRENCE_RATIO = 50

# おはようメッセージを作成する
def goodMorningMain( getMsgData ):
   
   msgRes = {}
   msgRes['type'] = getMsgData['type']

   # 挨拶作成
   msgRes['isMorningMsg'] = True
   msgRes['morningMsg'] = greeting.greetingMain()

   # スタンプ作成
   if random.randint( 0, 99) < STAMP_OCCURRENCE_RATIO:
      msgRes['isStamp'] = True
      msgRes['stampMsg'] = stamp.stampMain()
   else:
      msgRes['isStamp'] = False

   # 天気予報作成
   msgRes['isWeatherMsg'] = True
   msgRes['WeatherMsg'] = weatherForecast.weatherForecastMain()
   
   return msgRes
