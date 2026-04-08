class A:
    def __init__(self):
        self.public = 1
        self._protected = 2
        self.__private = 3

obj = A()
print(obj.public)        # OK
print(obj._protected)    # OK (not recommended)
# print(obj.__private)   # Error