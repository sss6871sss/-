import requests
from bs4 import BeautifulSoup
from datetime import datetime
import jtalk as j

def generate_weather_text():
    # tenki.jpの目的の地域のページURL（大阪府大阪市）
    url = 'https://tenki.jp/forecast/6/30/6200/27100/'

    #HTTPリクエスト
    r = requests.get(url)

    #プロキシ環境下の場合は以下を記述
    """
    proxies = {
    	#自分のプロキシのアドレスを記述
    	"http":"http://proxy.xxx.xxx.xxx:8080",
    	"https":"http://proxy.xxx.xxx.xxx:8080"
    }
    r = requests.get(url, proxies=proxies)
    """

    bsObj = BeautifulSoup(r.content, "html.parser")
    today = bsObj.find(class_="today-weather")
    weather = today.p.string
    
    #気温情報のまとまり
    temp=today.div.find(class_="date-value-wrap")
    
    #気温の取得
    temp=temp.find_all("dd")
    temp_max = temp[0].span.string #最高気温
    temp_max_diff=temp[1].string #最高気温の前日比
    temp_min = temp[2].span.string #最低気温
    temp_min_diff=temp[3].string #最低気温の前日比
    
    #結果の出力
    print("天気:{}".format(weather))
    print("最高気温:{} {}".format(temp_max,temp_max_diff))
    print("最低気温:{} {}".format(temp_min,temp_min_diff))
    text = "今日の天気は、"+ weather + "、です。" + "最高気温は、" + temp_max + "度です。最低気温は、" + temp_min + "度です。"
    return text

def generate_greeting_text():
    d = datetime.now()
    hour = d.hour
    if hour >= 17 :
        text = "こんばんわ。"
    elif hour >= 12:
        text = "こんにちわ。"
    else:
        text = "おはようございます。"
    return text

if __name__ == '__main__':
    text = generate_weather_text()
    j.jtalk(text)
