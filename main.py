class Parent:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
        #print(self.__name)
    def method2(self):
        print(self.name)
class Child (Parent):
    def method1(self):
        print(self._Parent__name)

if __name__ == "__main__":
    obj = Child("naveen", 23)
    obj.method1()
