# 创建集合
Days = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
Months = {'Jan', 'Feb', 'Mar'}
Dates = {21, 22, 17}
print(Days)
print(Months)
print(Dates)

# 访问集合中的值
# 无法访问集合中的单个值，只能如上所示访问所有元素，但是也可以通过遍历改集合来获取单个元素的列表
for d in Days:
    print(d)

# 将项目添加到集合：add() 方法
Days.add('Sun')
print(Days)

# 从集合中删除项目：discard()
Days.discard('Fri')
print(Days)

# 集合 并集
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA | DaysB
print(AllDays)

# 集合 交集
AllDays = DaysA & DaysB
print(AllDays)

# 集合 差集
AllDays = DaysA - DaysB
print(AllDays)

# 比较集合  检查一个给定的集合是否是另一个集合的子集或超集。 结果是True或False
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
