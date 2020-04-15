import json
import requests

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

def get_data(url):
    response=requests.get(url,headers=headers)
    print(response.text)
    return response.text

def parse_data(html):
    text=json.loads(html)
    items=text['data']['list']['vlist']
    print(items)
    for item in items:
        yield {
            '标题':item['title'],
            'bv号':item['bvid'],
            '评论数':item['comment'],
            '播放数':item['play'],
            '视频链接':item['pic'],
            '视频长度':item['length']
        }

def write_data(content):
    with open('花丸视频数据.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(page):
    url='https://api.bilibili.com/x/space/arc/search?mid=441381282&ps=30&tid=0&keyword=&order=pubdate&jsonp=jsonp'
    url=url+'&pn='+str(page)
    html=get_data(url)
    parse_data(html)
    for item in parse_data(html):
        write_data(item)

for i in range(1,4):
    main(i)