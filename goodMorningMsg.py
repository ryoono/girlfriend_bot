# -*- coding: utf-8 -*-

import greeting

def goodMorningMain( getMsgData ):
   
   msgRes = {}
   msgRes['isMorningMsg'] = True

   msgRes['morningMsg'] = greeting.greetingMain()
   msgRes['isStamp'] = False
   msgRes['isWeatherMsg'] = False
   
   return msgRes
