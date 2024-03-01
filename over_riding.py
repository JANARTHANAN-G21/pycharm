class employee:

    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 40

    def displaythenumberofworkinghours(self):
        print(self.setnumberofworkinghours)

class Trainee(employee):

    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 45

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

employee = employee()
employee.setnumberofworkinghours()
print("number of working hours of emps:", end = " ")
employee.displaythenumberofworkinghours()

trainee = Trainee()
trainee.setnumberofworkinghours()
print("number of working hours of trainee,",end = " ")
trainee.displaythenumberofworkinghours()

trainee.resetnumberofworkinghours()
print("number of working hours has been reset:",end = " ")
trainee.displaythenumberofworkinghours()
