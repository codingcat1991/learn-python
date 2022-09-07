"""
自动从文本中提取电子邮件
content =”"
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作python666@163.cn者：贾岛
松下问童子，言师python-abc@163com采药去。
只在python_ant-666@sina.net此山中，云深不知处。
"""
import re

content = """
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作python666@163.cn者：贾岛
松下问童子，言师python-abc@163com采药去。
只在python_ant-666@sina.net此山中，云深不知处。
"""

pattern = re.compile(r'''[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}''', re.VERBOSE)
print(pattern.findall(content))
