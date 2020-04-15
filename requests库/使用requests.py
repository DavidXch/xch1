import requests
import re
response=requests.get('http://bilibili.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

#二进制数据抓取
r = requests.get("https://img.qingwk.com/images/cover/global/2020/03/16/103812_92881225256_528x396.jpg")
print(r.content)
with open('../urllib/test.jpg', 'wb') as f:
    f.write(r.content)

r1=requests.get("https://www.qingwk.com")
print(r1.headers)
print(r1.cookies)

content="dfi344fifj38rfj483jfld"
content=re.sub('\d','',content)#sub会删除替换所有匹配到的项目
print(content)