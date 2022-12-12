# # coding = utf-8
#
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # property装饰器， 访问器——getter方法
    @property
    def name(self):
        return self._name

    # property装饰器， 访问器——getter方法
    @property
    def age(self):
        return self._age

    # property装饰器， 修改器——setter方法
    @age.setter
    def age(self, age):
        self._age = age

    # property装饰器， 修改器——setter方法
    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


if __name__ == '__main__':
    person = Person('王大锤', 12)
    person.play()
    person.age = 20
    person.play()
    person.name = '李桂英'
    person.age = 18
    person.play()



# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d * %d = %d" % (i,j,i*j), end=" \t")
#     print()





