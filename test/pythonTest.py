# 斐波那契数列
# 1 1 2 3 5 8 13 ...n
# import sys
# print(sys.getrecursionlimit())
# def fbn(n):
#     if n <= 2:
#         return 1
#     else:
#         return fbn(n - 1) + fbn(n - 2)
#
#
# print([fbn(i) for i in range(1, 11)])
import random

# def fibonacci(n):
#     lst = [0, 1]
#     if n == 0:
#         return [0]
#     for i in range(2, n + 1):
#         lst.append(lst[i - 1] + lst[i - 2])
#     return lst
#
#
# print(fibonacci(10))
# range_ = [x * 2 for x in range(1,11)]
# print(range_)
# def fbn(n):
#     if n <= 2:
#         return 1
#     else:
#         return fbn(n - 1)+fbn(n-2)
#
#
# print([fbn(i) for i in range(1,10)])

# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
#
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if x * 5 + y * 3 + z / 3 == 100:
#             print("公鸡:%d只，母鸡:%d只，小鸡:%d只" %(x, y, z))


# sum = 0
# for x in range(1, 101):
#     sum += x
# print(sum)
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)
# sum = 0
# for x in range(1, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

# answer = random.randint(1, 101)
# counter = 0
# while True:
#     counter += 1
#     number = int(input("请输入:"))
#     if number < answer:
#         print("输小了")
#     elif number > answer:
#         print("输大了")
#     else:
#         print("恭喜你猜对了")
#         break
# print("你总共猜了%d次" % counter)
# if counter > 7:
#     print("你的智商明显不足")

# 99乘法表决
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d" % (i, j, i*j), end='\t')
    print()
"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束"""
money = 1000
while money > 0:
    print("你的总资产为：", money)
    needs_go_on = False
    while True:
        debt = int(input("请下注："))
        if 0 < debt <= money:
            break
    first = random.randint(1, 6) + random.randint(1, 6)
    print("玩家摇出了%d点" % first)
    if first == 7 or first == 11:
        print("玩家获胜")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print("庄家获胜")
    else:
        needs_go_on = True
    while needs_go_on:
        current = random.randint(1, 6) + random.randint(1, 6)
        print("玩家摇出了%d点" % current)
        if current == 7:
            print("庄家获胜")
            money -= debt
            needs_go_on = False
        elif current == first:
            print("玩家获胜")
            money += debt
            needs_go_on = False
print("你破产了，游戏结束!")































