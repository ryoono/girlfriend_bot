# -*- coding: utf-8 -*-

import myConst

import os
import sys
import requests
from bs4 import BeautifulSoup
import json

from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage, StickerSendMessage
)

# 環境変数を参照し変数に格納
channel_access_token = os.getenv( 'LINE_CHANNEL_ACCESS_TOKEN', None)
user_id = os.getenv( 'LINE_USER_ID', None)
mebo_api_key = os.getenv( 'MEBO_API_KEY', None)
mebo_agent_key = os.getenv( 'MEBO_AGENT_KEY', None)
mebo_uid = os.getenv( 'MEBO_UID', None)

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)
if user_id is None:
    print('Specify LINE_USER_ID as environment variable.')
    sys.exit(1)
if mebo_api_key is None:
    print('Specify mebo_api_key as environment variable.')
    sys.exit(1)
if mebo_agent_key is None:
    print('Specify mebo_agent_key as environment variable.')
    sys.exit(1)
if mebo_uid is None:
    print('Specify mebo_uid as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi( channel_access_token )

# 引数の1時間天気予報を取得する
def getTenki_jp( url ):
    
    r = requests.get( url )
    html = r.text.encode( r.encoding )
    return BeautifulSoup( html, 'lxml')


# meboによってラインからのメッセージに対する返信を取得する
def getChatMsg( msg ):

    # リクエストに必要なパラメーター
   headers = { 'Content-Type':'application/json' }
   payload = { 'api_key':mebo_api_key, 'agent_id':mebo_agent_key, 'utterance':msg, 'uid':mebo_uid}
   url = 'https://api-mebo.dev/api'

   # APIを叩く
   res = requests.post( url=url, headers=headers, data=json.dumps(payload))

   # 最適と思われるレスポンスを抽出
   return res.json()['bestResponse']['utterance']


# ラインにメッセージを送信する
def sendPushLineMsg( msgRes ):

    # おはようメッセージの場合、
    if msgRes['type'] == myConst.MORNING_WEEKDAY_MSG_TYPE or msgRes['type'] == myConst.MORNING_HOLIDAY_MSG_TYPE:
        if msgRes['isMorningMsg'] == True:
            morningMsg = msgRes['morningMsg']
            line_bot_api.push_message( user_id, messages=TextSendMessage(text=morningMsg))
        
        if msgRes['isStamp'] == True:
            stampNum = StickerSendMessage(package_id=msgRes['stampMsg'][0], sticker_id=msgRes['stampMsg'][1])
            line_bot_api.push_message( user_id, messages=stampNum)
            
        if msgRes['isWeatherMsg'] == True:
            weatherMsg = msgRes['WeatherMsg']
            line_bot_api.push_message( user_id, messages=TextSendMessage(text=weatherMsg))

    elif msgRes['type'] == myConst.CHAT_MSG_TYPE:
        line_bot_api.reply_message(
            msgRes['reply_token'],
            msgRes['res_mes']
        )