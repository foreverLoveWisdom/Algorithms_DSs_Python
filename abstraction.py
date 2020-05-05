from abc import ABC, abstractmethod

"""
* Abstraction is the process of separating the presentation details
    from the implementation details.
    
* This is done so that the developer is relieved of the
    more complex implementation details.
        Instead, the programmer can focus on the presentation or
            the behavioral details of the entity.
    
    => Focuses on how a certain entity can be used rather than
        how it is implemented. 

* Abstraction essentially hides away the implementation details,
    so that even if the implementation methodology changes
        over time, programmer would not have to worry how
            it would affect his program.

* Abstraction is a technique, which helps us to identify what should be
    visible and what should be hidden.

* Encapsulation is the techniques for packaging the information such that
    it makes visible what should be visible and hides what
        should be hidden. 

* In other words, Encapsulation can be identified as
    one step beyond abstraction.
        - While abstraction reduces a real world object to
            its essential defining characteristics,
                encapsulation extends this idea by
                    modeling and linking this functionality of that
                    entity.
                    
* Abstraction in Python is achieved by using abstract classes and interfaces.

* An interface should just provide the method names without method bodies.
    - Subclasses should provide implementation for all the methods defined
        in an interface.
        - Note that in Python there is no support for creating
            interfaces explicitly, you will have to use abstract class.
                - In Python you can create an interface using abstract class.
                    - If you create an abstract class which
                        contains only abstract methods that acts as
                            an interface in Python.
                            
* In software engineering and computer science, abstraction is:
    - The process of removing physical, spatial, or
        temporal details or attributes in the study of objects or
            systems to focus attention on details of greater importance;
                - It is similar in nature to the process of generalization;
    
    - The creation of abstract concept-objects by mirroring common features
        or attributes of various non-abstract objects or
            systems of study – the result of the process of abstraction.
"""


class Payment(ABC):
    def print_slip(self, amount):
        print("Purchase of amount: ", amount)

    @abstractmethod
    def payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def payment(self, amount):
        print("Credit card payment of - ", amount)


class MobileWalletPayment(Payment):
    def payment(self, amount):
        print("Mobile wallet payment of - ", amount)


obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment))

obj = MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)
print(isinstance(obj, Payment))
