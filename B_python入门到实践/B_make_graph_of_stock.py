from __future__ import  (absolute_import,division,print_function,unicode_literals)

try:
    from  urllib import  urlopen
except ImportError:
    from  urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

response = urlopen(json_url)
#读取数据源
req = response.read()
#写入数据
with open('btc_close_2017.json', 'w') as f:
    f.write(req)
#加载json格式
file_urlib = json.loads(req)
print(file_urlib)