"""
统计每个兴趣的学生人数
小张 篮球,羽毛球
小王 篮球,乒乓球
小李 篮球,台球
小赵 篮球,足球,台球
小马 乒乓球,台球
小钱 羽毛球,足球
小孙 乒乓球,台球
小强 羽毛球
"""
from collections import defaultdict


def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content


def parse_content(content: str):
    likes = defaultdict(set)
    for row in content.split('\n'):
        name, like = row.split(' ')
        for item in like.split(','):
            likes[item].add(name)
    for like, names in likes.items():
        print(f'{like}:{len(names)}')


c = read_file('t-ike')
parse_content(c)
