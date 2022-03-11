# -*- coding: utf-8 -*-

import commMng

# チャット(返信)メッセージ作成
def chatMain( getMsgData ):
   
   msgRes = {}
   msgRes['type'] = getMsgData['type']
   msgRes['reply_token'] = getMsgData['reply_token']
   msgRes['res_mes'] = commMng.getChatMsg( getMsgData['msg'] )

   return msgRes

