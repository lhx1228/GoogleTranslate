import json
import requests
import re
from bs4 import BeautifulSoup
from get_tk import Py4Js

def main(Word):   #获取tk值
    js = Py4Js()

    content = Word

    tk = js.getTk(content)

    res = translate(Word,tk)
    return res


def translate(Word,tk):
    res = requests.get('https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk={}&q={}'.format(tk,Word))  #汉转英
    d = res.json()
    if d[0][0][0] == Word:
        res = requests.get('https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk={}&q={}'.format(tk,Word))  # 英转汉
        d = res.json()
    #print(d[0][0][0])
    return d[0][0][0]

if __name__ == '__main__':
    main(Word)
