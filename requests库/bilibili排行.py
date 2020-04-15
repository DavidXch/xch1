import requests
import json
import re

def get_imformation(url):
    try:
        headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            #print(response.text)
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None

def parse_imformation(html):
    #pattern=re.compile('"rank-item".*?"num">(\d+)</div>.*?href="(.*?)".*?href="(.*?)".*?"title">(.*?)</a>.*?info">(.*?)</div></i>(.*?)</span.*?</i>(.*?)</span.*?</i>(.*?)</span.*?pts.*?div>(.*?)</div>',re.S)
    items=re.findall('"rank-item".*?"num">(.*?)</div>'
                     +'.*?"img".*?href="(.*?)"'
                     +'.*?"info".*?href="(.*?)"'
                     +'.*?"title">(.*?)</a>'
                     +'.*?"pgc-info">(.*?)</div>'
                     +'.*?"b-icon play"></i>(.*?)</span>'
                     +'.*?"b-icon view"></i>(.*?)</span>'
                     +'.*?"fav"></i>(.*?)</span>'
                     +'.*?"pts"><div>(.*?)</div>',html,re.S)
    print(items)
    for item in items:
        yield {
            'rank':item[0],
            'image url':item[1],
            'cartoon url':item[2],
            'name':item[3],
            'status':item[4],
            '播放量':item[5],
            '评论数量':item[6],
            '追番人数':item[7],
            '综合评分':item[8]
        }

def write_to_file(content):
    with open('bilibilitest.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main():
    url='https://www.bilibili.com/ranking/bangumi/13/0/3'
    html=get_imformation(url)
    parse_imformation(html)
    for item in parse_imformation(html):
        print(item)
        write_to_file(item)

main()