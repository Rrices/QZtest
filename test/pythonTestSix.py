"""
coding = utf-8
pythonTestSix - 
Author: yh
Date: 2022/12/8
"""

total = float(input("本月收入: "))
Insurance = float(input("五险一金: "))
E = total - Insurance
i = E - 3500
if 0 < i <= 1500:
    R = 0.03
    D = 0
elif i <= 4500:
    R = 0.1
    D = 105
elif i <= 9000:
    R = 0.2
    D = 555
elif i <= 35000:
    R = 0.25
    D = 1005
elif i <= 55000:
    R = 0.3
    D = 2755
elif i <= 80000:
    R = 0.35
    D = 5505
else:
    R = 0.45
    D = 13505
if i > 0:
    T = i * R - D
else:
    T = 0

print(f"应纳税款：{T:.2f}")
print(f"税后收入：{E-T:.2f}")














