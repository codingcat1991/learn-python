"""
提取小说中的人名
"""
import collections

content = "李明喜欢韩梅梅，他俩早恋了"

from jieba import posseg

words = []
for word, flag in posseg.cut(content):
    if flag == 'nr':
        words.append(word)

counter = collections.Counter(words)
print(counter.most_common(2))
