# -*- coding: utf-8 -*-

import chatbotMain
import myConst

if __name__ == "__main__":
    
    # あいさつメッセージ用
    msgInfo = {}
    msgInfo['type'] = myConst.MORNING_WEEKDAY_MSG_TYPE

    # msgInfo = {}
    # msgInfo['type'] = myConst.CHAT_MSG_TYPE
    # msgInfo['msg'] = "こんばんは"
    # msgInfo['reply_token'] = "-"

    chatbotMain.chatbotMain( msgInfo )
