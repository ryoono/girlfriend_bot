# -*- coding: utf-8 -*-

import chatbotMain
import myConst

if __name__ == "__main__":
    
    msgInfo = {}
    msgInfo['type'] = myConst.MORNING_WEEKDAY_MSG_TYPE
    chatbotMain.chatbotMain( msgInfo )
