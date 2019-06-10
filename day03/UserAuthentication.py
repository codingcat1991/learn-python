"""
用户省份认证
Author: zhouju
Version: 0.1
"""

username = str(input("请输入用户名："))
password = str(input("请输入密码："))

if username == "admin" and password == "123456":
    print("身份认证成功！")
else:
    print("身份认证失败！")
