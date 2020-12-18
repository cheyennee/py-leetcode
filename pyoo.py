#
#简单实例
#
class Turtle:
    color = 'green'
    weight = '10kg'
    legs = 4
    shell = True
    mouth = 'big'
    def climb(self):
        self.name = 'test'
        print('pa')
    def run(self):
        print('run')

tt = Turtle()
tt.climb()

#
#继承
#
class MyList(list):
    pass

list1 = MyList()
list1.append(1)



'''
构造
'''
class Ball:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print('I am %r'%self.name)

b = Ball('b')
b.kick()
