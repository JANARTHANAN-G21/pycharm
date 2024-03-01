class MethOperations:
    def add(self, a, b):
        return a + b

    def add(self,a , b, c):
        return a + b + c

math_ops=MethOperations()

result1 = math_ops.add(2, 3, 4)
print("result is:", result1)

result2 = math_ops.add(5, 6, 7)
print("New result is:",result2)
