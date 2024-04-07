import json
from suds.client import Client

wsdl_url = "http://127.0.0.1:9567/PyWebService/?wsdl"
client = Client(wsdl_url)  # 创建一个webservice接口对象
resp = client.service.get_version()  # 调用这个接口下的get_version方法，无参数
print(json.loads(resp))