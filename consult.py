class Doctor:
    def __init__(self,name,id,specialization,gender,sal):
        self.name=name
        self.id=id
        self.specialization=specialization
        self.gender=gender
        self.sal=sal
    def display(self):
        print(self.name)
        print(self.id)
        print(self.specialization)
        print(self.gender)
        print(self.sal)
class Patient:
    def __init__(self,name,address,problem,age,gender,fee):
        self.name=name
        self.address=address
        self.problem=problem
        self.age=age
        self.gender=gender
        self.fee=fee
    def details(self):
        print(self.name)
        print(self.address)
        print(self.problem)
        print(self.age)
        print(self.gender)
        print(self.fee)
class User:
    def __init__(self,name,id,docdetails,patientdetails,appointmentdate,time,availability):
        self.name=name
        self.id=id
        self.docdetails=docdetails
        self.patientdetails=patientdetails
        self.appointmentdate=appointmentdate
        self.time=time
        self.availability=availability
    def appointment(self):
        print(self.name)
        print(self.id)
        print(self.docdetails)
        print(self.patientdetails)
        print(self.appointmentdate)
        print(self.time)
        print(self.availability)
class Tests:
    def __init__(self,testid,reports,fees,patientname,testname):
        self.testid=testid
        self.reports=reports
        self.fees=fees
        self.patientname=patientname
        self.testname=testname
    def checkup(self):
        print(self.testid)
        print(self.reports)
        print(self.fees)
        print(self.patientname)
        print(self.testname)
class Medicine:
    def __init__(self,prescptid,nameofmed,availability,amount):
        self.prescptid=prescptid
        self.nameofmed=nameofmed
        self.availibility=availability
        self.amount=amount
    def prescription(self):
        print(self.prescptid)
        print(self.nameofmed)
        print(self.availibility)
        print(self.amount)
d1=Doctor('Albert',123,'cardioligist','male',20000)
d2=Doctor('Roger',213,'Dermatoligist','Female',12000)
d1.display()
d2.display()
p1=Patient('Sam','Banglore','Chest pain',45,'Male',3000)
p1.details()
e1=User('John',432,'123','sam','12/11/2000','2:00','available')
e1.appointment()
t1=Tests(432,'ECG',300,'sam','ECG')
t1.checkup()
m1=Medicine(543,'Telmidil','available',350)
m1.prescription()


