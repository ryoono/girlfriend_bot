import os
import sys
import numpy as np

import commMng

HARE = 0
KUMORI = 1
AME = 2

weatherTable = [
    '晴れてますね！今日は一日中晴みたいですよ！☀️',
    '今日もいい天気ですね！☀️',
    '夜は雨が降るみたいですよ！残業だったら傘を忘れずにね☔️',
    '☀️日中いい天候みたい☺️',
    '午前はいい天気みたいですね！',
    '夜は雨が降るみたいですね、、！折り畳み傘持ってった方がいいかも？？',
    '夕方雨降るかも？？☔️',
    '今日は夕方だけ雨が降るみたいですね、、、',
    '夕方から雨が降るみたいですよ...傘忘れないでね！',
    '今日もいい天気ですね！☀️気分いいです！笑',
    '今日はちょっとだけ曇りそうですねー☁️',
    '先輩！夜だけ雨降りそうですよ！☂️',
    '昼間は曇りそうですね！日焼け対策サボっても大丈夫でしょうか…？？',
    '今は晴れてるけどこれから曇るみたいですね🌤',
    '夜は雨っぽいですね、、せんぱい折り畳み傘持ちました？',
    '夕方に雨の予報ですよ！せんぱい天気予報見ましたか？？',
    'お昼から天気が怪しそうですよ。。。☹️☹️',
    '夕方からは雨が降るみたいですね、☔️',
    'お昼だけ雨降りそうですよ！夕方はやんでるみたい☺️☺️',
    'お昼少しふるみたいですね☂️！でも夕方は大丈夫そう、、、？？',
    'なんか微妙な天気ですよ、、傘忘れないようにしなきゃ☂️',
    'お昼に雨降りそうですね、、、夕方はやんでるといいなあ🙃',
    'お昼少しだけ雨降るみたいですね！夕方は大丈夫そう！☁️',
    '夕方だけ曇りみたいだけど帰り道は雨やんでるといいな！',
    '夕方は雨が降ってるっぽいですよ！先輩傘持ちました！？',
    'このあと雨降るみたいですね、、、☔️必須ですよ！',
    'お昼からずっと雨ですね、、、大学行きたくないなあ☔️😢',
    'これから晴れるみたいですね！☀️',
    '今日はまあまあいい天気みたいですよ⛅️',
    '夜少し雨降りそうですよ！残業だったら傘いるかもしれないですね！☔️',
    '今日は傘の心配いらなさそうですね！',
    '曇ってるみたいですね、、、夜は星が見えないかも⭐️',
    '夜だけ雨が降るみたいですよ☔️折り畳み傘いるかもしれないですね！',
    '夕方は雨が降るみたいですね、、、傘持ってく必要ありそうですね☂️',
    '夕方だけ雨が降りそうです、、、帰宅時間と被ってしまう泣泣',
    '夕方からは雨っぽいですね☔️傘を忘れないでくださいね！',
    'お昼からは晴れるみたいだから夜は星が見えるかもしれないですね！⭐️',
    'ザ・普通の天気ですよ！傘の心配はしなくてよさそうです⛅️',
    '夜だけ雨が降りそうですよ！せんぱい傘持ちました？？',
    '今は曇っているけど夜は晴れるみたいですね⭐️✨',
    'ずっと曇ってるみたいですね！珍しいかも☁️',
    '夜は雨降るっぽいです☔️いや夕方から怪しいかもですね…？？',
    '夕方だけ雨降るみたいですけど夜は星が見えそうですよ！⭐️',
    '夕方雨の予報ですけど降るんですかね？？☔️',
    '夕方から降るらしいですよ、、、嫌だなあ☔️',
    'お昼は雨ですけど帰る時間にはやんでそう！ラッキーですね笑',
    'お昼だけ雨降るみたいですけど帰る時間にはやんでそうですね☀️',
    'なんか変な天気ですよ、、、雨が降るのかよく分かりませんね🤔',
    'お昼は雨降るみたいですね、、、夕方も微妙かも☁️',
    '一日中微妙な天気っぽいですね、、、移動中は雨降りませんように🥺',
    '雨が降ったりやんだりしそうですね☔️滑らない様に気をつけてくださいね笑',
    'なんか雨が降るみたいですけど夜は晴れるみたいですよ！⭐️',
    'お昼から降ってきそうです☔️大学行きたくないな、、、',
    '昼から雨降るみたいですよ☔️先輩の会社まではもちますように😘',
    'お昼からは晴れるみたいですよ！帰り道は安心ですね☀️',
    '行きは降られそうですね、、、帰りに傘を忘れちゃいそうです😥',
    '昼は晴れるみたいだけど夜はまた雨が降るみたいですね☔️',
    'これから晴れていくみたいですね！夜は星見えるかな⭐️',
    '雨、お昼にはあがるみたいですよ！',
    'お昼はやむけど夜はまた降るみたいですね、、、夜は晴れてるといいな',
    '変な天気！雨晴雨晴ですよ！☀️☔️',
    'お昼は一瞬晴れるみたいですね☀️夕方は雨っぽいです！😢',
    'お昼だけ晴れるみたいですね！ずっと雨よりはマシですかね…？？',
    'この雨があがったらずっと晴れてそうですよ！ラッキーですね😄',
    '雨はこの後やむみたいですね！晴れて欲しい！☀️',
    '夜にまた雨が降りそうですね、、、残業あるなら気をつけてくださいね！',
    '帰り道は晴れてそうですね☀️よかったです！😀😄',
    '雨がやんでもずっと曇りみたいですよ、、、どんよりですね🙃',
    '一日中天気が怪しいですよ！雨に注意した方がいいかもですね、、、🙃',
    '朝も夕方も雨の予報ですよ！これは困った😢',
    '移動中は雨っぽいですね、、、水溜りに注意してくださいよ笑',
    '今日は1日雨っぽいから事故とかに気をつけてくださいね🚗',
    '夕方から晴れるみたいですよ！帰りは傘いらないかな⭐️',
    'お昼過ぎからは雨がやむみたいですね！帰り道は傘ささなくてもよさそう😄',
    '夕方だけ雨があがりそうですよ！帰り道は晴れてますように🥺',
    'お昼からは晴れそうですね！夕方は傘なくても大丈夫かな☂️',
    '夕方からは雨があがるみたいですよ！やんでるといいな！',
    '今日はずっと雨だから気分下がっちゃいますね😢',
    '夜だけ晴れるみたいだけど、もしかしたら星が見えるかもしれないですね！⭐️',
    '今日はずっと雨みたいですね、、、動きたくないー😩',
    '今日はずっと雨が降ってるみたいだから、傘を忘れないでね！☔️'
]

tenki_url = os.getenv('TENKI_URL', None)
if tenki_url is None:
    print('Specify TENKI_URL as environment variable.')
    sys.exit(1)

WeatherClassificationTable = {}
WeatherClassificationTable['晴れ'] = HARE
WeatherClassificationTable['曇り'] = KUMORI
WeatherClassificationTable['不明'] = KUMORI
WeatherClassificationTable['小雨'] = AME
WeatherClassificationTable['弱雨'] = AME
WeatherClassificationTable['雨'] = AME
WeatherClassificationTable['強雨'] = AME
WeatherClassificationTable['豪雨'] = AME
WeatherClassificationTable['乾雪'] = AME  # 雪 未対応(雨としてカウント)
WeatherClassificationTable['湿雪'] = AME  # 雪 未対応(雨としてカウント)
WeatherClassificationTable['みぞれ'] = AME    # 雪 未対応(雨としてカウント)

# tenki.jpから今日の天気を取得し、天気に沿ったメッセージを返す
def weatherForecastMain():

    info = getWeatherInfo()
    infoNum = weather2num( info )
    tenkiCal = getTenkiCalculation( infoNum )
    tenkiMsg = getTenkiMsg( tenkiCal )

    return tenkiMsg

# 朝 ~ 夜までの天気から返信メッセージを計算する
def getTenkiMsg( tenkiCal ):

    weatherTableIndex = tenkiCal[0]*27 + tenkiCal[1]*9 + tenkiCal[2]*3 + tenkiCal[3]
    return weatherTable[weatherTableIndex]

# 朝 ~ 夜までの天気を計算する
def getTenkiCalculation( info ):

    timeStd = np.array([ [5,8], [8,14], [14,17], [17,21] ])
    res = []
    for i in range(0,4):
        buf = info[ timeStd[i][0] : timeStd[i][1] ]
        if AME in buf:
            res += [AME]
        else:
            if buf.count(HARE) >= buf.count(KUMORI):
                res += [HARE]
            else:
                res += [KUMORI]

    return res

# 1時~24時の天気(数字変換後)を返す
def weather2num( info ):
    
    res = []
    for i in range(0,24):
        res += [ WeatherClassificationTable[ info[i]['weather'] ] ]
    
    return res

# 日本気象協会より天気予報を取得して、時間ごとの天気を返す
def getWeatherInfo():

    s = commMng.getTenki_jp( tenki_url )

    soup_tdy = s.find( id='forecast-point-1h-today' )
    dict = {}
    dict = forecast2dict( soup_tdy )

    return dict['forecasts']

# 時間と天気を抜き出す
def forecast2dict(soup):

    data = {}

    # 一時間ごとのデータ
    # 時間と天気を取得
    hour    = soup.select('.hour > td')
    weather = soup.select('.weather > td')

    ## 格納
    data['forecasts'] = []
    for itr in range(0, 24):
        forecast = {}
        forecast['hour']    = hour[itr].text.strip()
        forecast['weather'] = weather[itr].text.strip()
        data['forecasts'].append( forecast )

    return data

# デバッグ用
if __name__ == '__main__':
    # info = [2,  # 1
    #         2,  # 2
    #         2,  # 3
    #         2,  # 4
    #         2,  # 5
    #         0,  # 6     朝
    #         0,  # 7     朝
    #         1,  # 8     朝
    #         0,  # 9     昼
    #         0,  # 10    昼
    #         0,  # 11    昼
    #         1,  # 12    昼
    #         1,  # 13    昼
    #         1,  # 14    昼
    #         0,  # 15    夕方
    #         0,  # 16    夕方
    #         1,  # 17    夕方
    #         0,  # 18    夜
    #         0,  # 19    夜
    #         1,  # 20    夜
    #         1,  # 21    夜
    #         2,  # 22
    #         2,  # 23
    #         2]  # 24
    # getTenkiCalculation(info)
    res = weatherForecastMain()
    # for i in range(0,81):
    #     print( weatherTable[i] )
    print(res)
