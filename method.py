# /Method overriding refers to ability of a subclass to provide a specific implementation
# of a method that is defined in its super class.
# when a method in a subclass has the same name, parameters and return type as a method in its superclass,
# method in the sub-class has the same name, parameters= and return type as method in its superclass
# the method in the subclass overrides the method in the super class.

# Diamond Quadram

class A:
    def method(self):
        print("method of class A")

class B(A):
    def method(self):
        print("method of class B")

class C(A):
    def method(self):
        print("method of class C")

class D(B,C):
    pass
d = D()
d.method()


#
