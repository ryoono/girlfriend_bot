# -*- coding: utf-8 -*-

import myConst
import goodMorningMsg
import chatMsg

# 作成するメッセージに応じて関数をCALLする
def massageMain( getMsgData ):

   # メッセージの種類を解析する
   # 固定メッセージの場合
   if getMsgData['type'] == myConst.FIXDE_MSG_TYPE:
      msgRes = 0

   # おはようメッセージの場合
   elif getMsgData['type'] == myConst.MORNING_WEEKDAY_MSG_TYPE or getMsgData['type'] == myConst.MORNING_HOLIDAY_MSG_TYPE:
      msgRes = goodMorningMsg.goodMorningMain( getMsgData )

   # チャットメッセージの場合
   elif getMsgData['type'] == myConst.CHAT_MSG_TYPE:
      msgRes = chatMsg.chatMain( getMsgData )

   # 画像メッセージの場合
   elif getMsgData['type'] == myConst.IMAGE_MSG_TYPE:
      msgRes = 3

   else:
      # 例外処理
      msgRes = 4

   return msgRes
