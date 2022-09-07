"""
中文分词
"""
import collections
import re

content = """
春姑娘悄悄地来到了我们的校园！
绿油油的小草争着抢着从地下探出头来，东张西望地看着四周。
池塘边的柳树，抽出了新的柳枝和柳叶，微风轻轻一吹，柳树就晃动着自己的秀发。
花园里各种各样的花儿都开了，
有艳红的玫瑰花、粉色的桃花、雪白的梨花.…五颜六色，美不胜收。
"""
import jieba

content = re.sub('\W', '', content)

words = jieba.cut(content)
counter = collections.Counter(words)
print(counter.most_common(2))
