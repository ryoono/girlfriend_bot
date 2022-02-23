# -*- coding: utf-8 -*-

import myConst

import os
import sys
import requests

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, MessageAction, TemplateSendMessage,
    ButtonsTemplate, StickerSendMessage
)

# 環境変数を参照し変数に格納
channel_secret = os.getenv( 'LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv( 'LINE_CHANNEL_ACCESS_TOKEN', None)
user_id = os.getenv( 'LINE_USER_ID', None)
chaplus_key = os.environ.get( "CHAPLUS_KEY")
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)
if user_id is None:
    print('Specify LINE_USER_ID as environment variable.')
    sys.exit(1)
if chaplus_key is None:
    print('Specify chaplus_key as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def sendLineMsg( msgRes ):

   if msgRes['type'] == myConst.MORNING_WEEKDAY_MSG_TYPE or msgRes['type'] == myConst.MORNING_HOLIDAY_MSG_TYPE:
      
      if msgRes['isMorningMsg'] == True:
         morningMsg = msgRes['morningMsg']
         line_bot_api.push_message(user_id, messages=TextSendMessage(text=morningMsg))
      
      if msgRes['isStamp'] == True:
         stampNum = StickerSendMessage(package_id=msgRes['stampMsg'][0], sticker_id=msgRes['stampMsg'][1])
         line_bot_api.push_message(user_id, messages=stampNum)

      # if msgRes['isWeatherMsg'] == True:

   # messages = TextSendMessage(text=str)
   # messages = StickerSendMessage(package_id='6325', sticker_id='10979918')
   # line_bot_api.push_message(user_id, messages=messages)