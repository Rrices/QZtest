"""
coding = utf-8
pythonTestNine - 
Author: yh
Date: 2022/12/8
"""
import math
# while True:
#     x = float(input("请输入三角形边长度x: "))
#     y = float(input("请输入三角形边长度y: "))
#     z = float(input("请输入三角形边长度z: "))
#     if x + y > z and x + z > y and y + z > x:
#         m = x + y + z
#         d = (x + y + z) / 2
#         area = math.sqrt(d * (d - x) * (d - y) * (d - z))
#         print("该三角形的面积是:%.2f" % area)
#         print("该三角形的周长是:%.2f" % m)
#         break
#     else:
#         print("不能构成三角形，请重新输入!")

for time in range(3, 0, -1):
    x = float(input("请输入三角形边长度x: "))
    y = float(input("请输入三角形边长度y: "))
    z = float(input("请输入三角形边长度z: "))
    if x + y > z and x + z > y and y + z > x:
        m = x + y + z
        d = (x + y + z) / 2
        # 使用海伦公式求面积——>
        # area = (d * (d - x) * (d - y) * (d - z)) ** 0.5
        # 使用math库自带面积计算方法求面积
        area = math.sqrt(d * (d - x) * (d - y) * (d - z))
        print("该三角形的面积是:%.2f" % area)
        print("该三角形的周长是:%.2f" % m)
        break
    elif time - 1 > 0:
        print(f"您输入的长度无法构成三角形，请重新输入，您还剩余{time - 1}次机会")
    else:
        print("非常抱歉，您的次数已经用完！")

