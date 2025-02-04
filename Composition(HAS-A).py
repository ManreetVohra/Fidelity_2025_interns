#Car has Attributes name,color,model and it has method display which displays name,model and color
# Employee is another class which has attributes name, employee id and employee has a car

class Car:
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
    def display(self):
        print("Name   :",self.name)
        print("Model  :",self.model)
        print("Color  :",self.color)

class Employee:
    def __init__(self,emp_name,emp_id,car):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.car=car

c1=Car("Swift","Red","A123")
e1=Employee("Manreet","A785696",c1)
e1.car.display()