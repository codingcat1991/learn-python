"""
英制单位英寸和公制单位厘米互换
Author: zhouju
Version: 0.1
"""
value = float(input("请输入长度："))
unit = str(input("请输入单位："))
if unit == "in" or unit == "inch" or unit == "英寸":
    print("%.1fin = %.1fcm" % (value, value * 2.54))
elif unit == "cm" or unit == "centimeter" or unit == "厘米":
    print("%.1fcm = %.1fin" % (value, value / 2.54))
else:
    print("请输入正确的单位！")
