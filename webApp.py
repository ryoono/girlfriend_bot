# -*- coding: utf-8 -*-

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, MessageAction, TemplateSendMessage, ButtonsTemplate,
    ImageMessage, ImageSendMessage
)

import myConst
import chatbotMain

app = Flask(__name__)

# 環境変数を参照し変数に格納
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)

handler = WebhookHandler( channel_secret )

# Webhookからのリクエストをチェック(LINEトークから)
# LINEからはhttp://~/callbackに送信する設定になっている
@app.route("/callback", methods=['POST'])
def callback():

    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 署名を検証し、問題なければhandleに定義されている関数を呼び出す
    # 署名検証で失敗したときは例外をあげる
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    # handleの処理を終える
    return 'OK'

# Webhookからのリクエストをチェック(GASからのモーニング割り込み？)
# GASからはhttp://~/morningに送信する設定になっている
@app.route("/morning", methods=['POST'])
def morning():

    msgInfo = {}
    msgInfo['type'] = myConst.MORNING_WEEKDAY_MSG_TYPE
    chatbotMain.chatbotMain( msgInfo )

    return 'OK'
    

# LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に実行
# reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークン
# 第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクト
@handler.add(MessageEvent, message=TextMessage)
def message_text( event ):

    msgInfo = {}
    msgInfo['type'] = myConst.CHAT_MSG_TYPE
    msgInfo['msg'] = event.message.text
    msgInfo['reply_token'] = event.reply_token

    chatbotMain.chatbotMain( msgInfo )


# LINEでMessageEvent（画像を送信された場合）が起こった場合に実行
@handler.add(MessageEvent, message=ImageMessage)
def message_image( event ):

    msgInfo = {}
    msgInfo['type'] = myConst.MORNING_WEEKDAY_MSG_TYPE
    chatbotMain.chatbotMain( msgInfo )

    # msgInfo = {}
    # msgInfo['type'] = myConst.CHAT_MSG_TYPE
    # msgInfo['msg'] = event.message.text
    # msgInfo['reply_token'] = event.reply_token

    # chatbotMain.chatbotMain( msgInfo )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
