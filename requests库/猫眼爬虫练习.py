import requests
import json
import re
import time

def get_one_page(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
                 ,'Cookie':'__mta=147804680.1586530738061.1586534277464.1586534279527.8; uuid_n_v=v1; uuid=C96A38507B3B11EAAFBF93058EBA55BC8FE2021E1D274608AF162AA9CFE3F63E; _csrf=7f4b5977854d6aa2bebd59a54e2038fb7a6e8b4ec3eb4d22f10c3b138a5c79c3; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1586530731; mojo-uuid=53907690d47767f7a25d994c18556cba; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1716499cb77c8-041f39919badb3-396d7507-13c680-1716499cb77c8; _lxsdk=C96A38507B3B11EAAFBF93058EBA55BC8FE2021E1D274608AF162AA9CFE3F63E; mojo-session-id={"id":"714600c1e02411e458da81ea8d754a73","time":1586532569141}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1586534441; __mta=147804680.1586530738061.1586534279527.1586534441190.9; mojo-trace-id=14; _lxsdk_s=17164b5d04e-01b-873-9b2%7C%7C22'}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            print(response.text)
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?title="(.*?)".*?star">(.*?).*?time">(.*?)</p.*?integer">(.*?)</i.*?fraction">(.*?)</i.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{
            'rank':item[0],
            'image_url':item[1],
            'title':item[2],
            'actors':item[3],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_to_file(content):
    with open('../urllib/testresult1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(changepart):
    url='https://maoyan.com/board/4?offset='+str(changepart)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

for i in range(10):
    main(changepart=i*10)
    time.sleep(5)

#由于动态验证，失败TAT