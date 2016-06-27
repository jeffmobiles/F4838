# -*- coding: utf-8 -*-
#每天涨幅超过8-9.99%的.

from urllib import request
import json

#url http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=sort



top_url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=sort"

headers = {
'Content-Type': 'application/json'
}
webopen = request.urlopen(top_url)
webopen.headers = headers
web_file = webopen.read()
data = json.dumps(str(web_file))
print(data)