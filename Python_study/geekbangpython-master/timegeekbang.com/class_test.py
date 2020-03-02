# Python类的使用
# user1 = {'name':'tom','hp':100}
# user2 = {'name':'jerry','hp':80}
#
# def print_role(rolename):
#     print('name is %s  ,hp is %s' %(rolename['name'], rolename['hp']) )
#
# print_role(user1)


# Python创建一个基本类
# class Player():  # 定义一个类
#     # __init__ 这是类的实例化内置函数
#     def __init__(self, name, hp, occu):
#         # 类中属性使用 "__"《双下划线》修饰的属性是被封装过的,无法直接修改,只允许通过方法修改
#         self.__name = name  # 变量被称作属性
#         self.hp = hp
#         self.occu = occu
#
#     def print_role(self):  # 定义一个方法
#         print('%s: %s %s' % (self.__name, self.hp, self.occu))
#
#     def updateName(self, newname):
#         # 此方法可以修改类中私有属性
#         # self.__name = newname
#         # 此方式无法修改私有属性
#         self.name = newname


# user1 = Player('tom',100,'war')  #类的实例化
# user2 = Player('jerry',90,'master')
# user1.print_role()
# user2.print_role()
# user1.updateName('wilson')
# user1.print_role()
# user1.__name = ('aaa')
# user1.print_role()


# Python关于继承的使用
class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')


# Python中需要继承某类,定义类后在类的后面加上需要继承的类名
class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'Boss类怪物'

    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):
        print('我是怪物我怕谁')


a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(1)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
a3.whoami()

#  type() 函数可查看类型
print('a1的类型 %s' % type(a1))
print('a2的类型 %s' % type(a2))
print('a3的类型 %s' % type(a3))

# isinstance() 可判断一类是否是另一个类的子类
print(isinstance(a2, Monster))
