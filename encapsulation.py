"""
* Encapsulation is the process of wrapping data and operation that
    operate on them in to a single entity.

* In order to access data, certain predefined methods should be used.
    => encapsulated data are not directly accessible.
        => the integrity of data is preserved because the user is
            unable to directly access and modify the data
                as he/she wishes.

* The users will get or set the data values only through the methods that
    are publicly available to the users.
        => These methods usually provide data validation so that
            only the data in the appropriate format is allowed
                to be inserted in to the fields.
                
* The users of a class do not need to worry how its data are
    being stored and data access is restricted.
        => prevent data being modified by accident.
"""


class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Honda MSX 125"
        self.__updateSoftware()

    def drive(self):
        print("driving.__maxspeed: " + str(self.__maxspeed))

    # The sender can't send this message to the instance of this class.
    @staticmethod
    def __updateSoftware():
        print("updating software")


car = Car()
print(vars(car))
car.__maxspeed = 0
car.drive()
print(vars(car))
print(car.__maxspeed)

# Throws no attribute error
# car.__updateSoftware()
