"""
提取商品价格
"""
import re

content = """
小明上街买菜
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元;
买了3斤白菜花了5.4元；
"""

# 要求提取（1、黄瓜、8)、（2、葡萄、13.5)、(3、白菜、5.4）

pattern = re.compile('(\d)斤(.*)花了(\d(.\d))元')
for line in content.split('\n'):
    rst = pattern.search(content)
    print(f"{(rst.group(1), rst.group(2), rst.group(3))}")
