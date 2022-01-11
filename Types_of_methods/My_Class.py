class MyClass:
    x = 10

    def method(self):
        return "Instance method called", self

    @classmethod
    def class_method(cls):
        return "Class method called", cls

    @staticmethod
    def static_method():
        return "Class method called"


'''
Instance methods -> can freely access attr and methods on the same object.

'''
