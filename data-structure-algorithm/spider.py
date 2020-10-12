# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 20:01
# @Author  : JacobZhou
# @Email   : JacobZhou@canway.net
# @File    : spider.py
# @Project : AlgorithmInterview
import json

import requests

url = "https://zb.oschina.net/project/contractor-browse-project-and-reward?applicationAreas=&sortBy=30&currentTime=&pageSize=20&currentPage=1"
resp = requests.get(url)
data = json.loads(resp.content)["data"]
total_count = data["totalCount"]
url = "https://zb.oschina.net/project/contractor-browse-project-and-reward?applicationAreas=&sortBy=30&currentTime=&pageSize=" + str(
    total_count) + "&currentPage=1"
resp = requests.get(url)
data = json.loads(resp.content)["data"]["data"]
today = []
# for item in data:
#     if item['publishTime'].startswith('2020-09-22'):
#         today.append(item)
# print(len(today))
# print(today)
# for item in data:
#     detail_url = "https://zb.oschina.net/project/detail?id=" + str(item['id'])
#     detail_resp = requests.get(detail_url)
#     detail_data = json.loads(detail_resp.content)
#     print(detail_data)

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "accept": "application/json",}
resp = requests.get("https://codemart.com/api/project?page=3", headers=Headers)
print(json.loads(resp.content))
