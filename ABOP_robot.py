class Robot:
    population = 0 #ПЕРЕМЕННАЯ КЛАССА

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'.format(Robot.population))

    def sayHi(self):
        print('Приветики! Я {0}'.format(self.name))

    def howMany():
        print('У нас {0:d} роботов'.format(Robot.population))

    howMany = staticmethod(howMany)
    
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('Роботы работают')
print('Роботы поработали, выпилим их')

del droid1
del droid2

Robot.howMany()
