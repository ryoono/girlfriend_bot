# -*- coding: utf-8 -*-

import myConst
import goodMorningMsg

def massageMain( getMsgData ):

   # メッセージの種類を解析する
   if getMsgData['type'] == myConst.FIXDE_MSG_TYPE:
      msgRes = 0

   elif getMsgData['type'] == myConst.MORNING_MSG_TYPE:
      msgRes = goodMorningMsg.goodMorningMain( getMsgData )

   elif getMsgData['type'] == myConst.CHAT_MSG_TYPE:
      msgRes = 2

   elif getMsgData['type'] == myConst.IMAGE_MSG_TYPE:
      amsgRes = 3

   else:
      # 例外処理
      msgRes = 4

   return msgRes
