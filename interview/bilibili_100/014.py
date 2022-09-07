"""
统计英文文章出现最多的单词次数
"""
import collections
import re


def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content


def split_content(content: str):
    words = re.split(r'\W', content)
    words = [word for word in words if word]
    return words


def count_word(words, word):
    return collections.Counter(words)[word]


def max_count(words):
    return collections.Counter(words).most_common()[1]


content = read_file('article')
words = split_content(content)
print(max_count(words))
