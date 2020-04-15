import urllib.request
import urllib.error
import urllib.parse
import socket
#异常处理
try:
    response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
except urllib.error.URLError as e:
    print(e.reason)
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("ohhhh,no!!!!!!!!")

#urlparse类(实现url的识别和分段)
result=urllib.parse.urlparse("https://t.bilibili.com/?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.29")
print(type(result))
print(result)

#parse.quote用法：转换中文至url可识别的格式
keyword="我爱爬虫"
print(urllib.parse.quote(keyword))
print(urllib.parse.unquote("%E6%88%91%E7%88%B1%E7%88%AC%E8%99%AB"))