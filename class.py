class Employee:
    def __init__(self,name,id,sal,dept):
        self.name=name
        self.id=id
        self.sal=sal
        self.dept=dept
    def display(self):
        print(self.name)
        print(self.id)
        print(self.sal)
        print(self.dept)
class Timesheet:
    def __init__(self,date,noofhrs,activity,description,status):
        self.date=date
        self.noofhrs=noofhrs
        self.activity=activity
        self.description=description
        self.status=status
    def details(self):
        print(self.date)
        print(self.noofhrs)
        print(self.activity)
        print(self.description)
        print(self.status)
e1=Employee('sam',321,40000,'cse')
e1.display()
p1=Timesheet('12/11/2000',4,'completed','hello','finish')
p1.details()



