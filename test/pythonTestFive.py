# coding = utf-8
# import math
# r = float(input("请输入r:"))
# l = 2 * math.pi * r
# a = math.pi * r ** 2
# print(f"长为:{l:.2f}")
# print(f"面为:{a:.2f}")
import getpass
username = input("请输入账号：")
# getpass方法只能使用终端（Terminal）进行运行
password = getpass.getpass("请输入密码：")
if username == 'admin' and password == 'Admin123':
    print('登录成功')
else:
    print("账号或密码错误")








