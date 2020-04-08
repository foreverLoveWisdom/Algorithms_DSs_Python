class Base:

    def fun(self):
        print("Public Method")

    def __fun(self):
        print("Private Method")

    def i_am_happy(self):
        self.__fun()


class Derived(Base):
    def _init__(self):
        Base.__init__(self)

    def call_public(self):
        print("\nInside derived class")
        self.fun()

    def call_private(self):
        self.__fun()


obj1 = Base()

# obj2 = Derived()
# print(obj2.call_public())
print(obj1.i_am_happy())
