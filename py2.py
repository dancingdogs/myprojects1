#                          ENCAPSULATION
'''
class Student:
    def __init__(self):
        self.__id=123
        self.__name="John"
    def display(self):
        print(self.__id)
        print(self.__name)


s=Student()
s.display()
'''
'''
class Student2:
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
    


s=Student2()
s.setId(123)
s.setName("John")
print(s.getId())
print(s.getName())

'''


#                   INHERITANCE
'''
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

     
    
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        #BMW.__init__(self,make,model,year)
        super().__init__(make,model,year)
        self.cruiseControlEnabled= cruiseControlEnabled
    def display(self):
        print(self.cruiseControlEnabled)
    def start(self):
        super().start()
        print("Button Start")  #overriding
            
     


class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        #BMW.__init__(self,make,model,year)
        super().__init__(make,model,year)
        self.parkingAssistEnabled= parkingAssistEnabled 
    def display(self):
        print(self.parkingAssistEnabled)
     


threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)



fiveSeries=FiveSeries(True,"BMW","E60","2019")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)


threeSeries.start()
threeSeries.stop()
threeSeries.display()


'''
#                      POLYMORPHISM

#                      DUCK TYPING
'''
class Duck:
    def talk(self):
        print("Quack Quack")
    
class Human:
    def talk(self):
        print("Hello")

def callTalk(obj):
    obj.talk()

d=Duck()
h=Human()

callTalk(d)
callTalk(h)
'''
#                    Dependency Injection
'''
class Flight:
    def __init__(self,engine):
        self.engine=engine
    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")
    
class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")

ae=AirbusEngine()
f=Flight(ae)
f.startEngine()

be=BoeingEngine()
f1=Flight(be)
f1.startEngine()
'''