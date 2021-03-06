import requests
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime
import generateText as gt

def jtalk(text):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(text.encode())
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr=subprocess.Popen(aplay)

def talk_weather():
    text = gt.generate_weather_text()
    jtalk(text)

def talk_greeting():
    text = gt.generate_greeting_text()
    jtalk(text)