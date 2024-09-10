from typing import Any


class Human:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hello! my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp= xp
    
class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team=fav_team


sol = Player("sol", 1000)

sol.say_hello()
print(sol.name, sol.xp)

class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self): #class가 보이는 방식을 커스터마이징한다.
        print(super().__str__())  #<__main__.Dog object at 0x107f14650>
        return f"Dog : {self.name}" #Dog : jia
    def woof(self):
        print("woof woof")
    def __getattribute__(self, name):
        #속성이 어떤 값을 가지고 있는지 보여주는 역활을 맡고 있다.
        print(f"They want to get {name}")
        #인스턴스의 name속성에 접근하면 return 값을 반환한다.
        
        return "accese to name value what you want to return"
    
jia = Dog("jia")
print(jia)

class Beagle(Dog):
    def woof(self):
        super().woof()
        print("under woof!!")

#beagle = Beagle()
#beagle.woof()
