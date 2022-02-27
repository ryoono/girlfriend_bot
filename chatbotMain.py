# -*- coding: utf-8 -*-

import messageMain
import commMng

def chatbotMain( getMsgData ):

   msgRes = messageMain.massageMain( getMsgData )

   commMng.sendPushLineMsg( msgRes )
