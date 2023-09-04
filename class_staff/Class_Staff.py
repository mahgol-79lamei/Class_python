#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Staff:
    def __init__(self, frstnm, lstnm, hrs, insrnc, numOfMls):
        self.firstName = frstnm
        self.lastName = lstnm
        self.workingHours = hrs
        self.insurance = insrnc
        self.numberOfMeals = numOfMls
        self.salary = 0

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName


class Manager(Staff):
    def __init__(self, fn, ln, hs, ins, meals):
        super().__init__(fn, ln, hs, ins, meals)

    def computeMealsPrice(self):
        return self.numberOfMeals * 12000

    def computeSalary(self):
        sa = 0
        hours = self.workingHours
        if hours > 100:
            hours = hours - 100
            sa = 100 * 100000
            sa = sa + hours * 80000
        else:
            sa = hours * 100000
        if self.insurance == True:
            sa = sa - 250000
        sa = sa - self.computeMealsPrice()
        self.salary = sa
        return self.salary


class Employee(Staff):
    def __init__(self, fn, ln, hs, ins, meals):
        super().__init__(fn, ln, hs, ins, meals)

    def computeMealsPrice(self):
        return self.numberOfMeals * 9000

    def computeSalary(self):
        sa = 0
        hours = self.workingHours
        if hours > 80:
            hours = hours - 80
            sa = 80 * 70000
            sa = sa + hours * 85000
        else:
            sa = hours * 70000
        if self.insurance == True:
            sa = sa - 180000
        sa = sa - self.computeMealsPrice()
        self.salary = sa
        return self.salary


mngrA = Manager("John", "Bolton", 150, True, 19)
mngrB = Manager("Anna", "Calderon", 80, True, 15)
mngrC = Manager("Alex", "Cole", 110, False, 21)
emplyA = Employee("Robert", "Neville", 75, True, 25)
emplyB = Employee("Sonya", "Carter", 90, False, 25)
print("Staff salary report\n--------------------------------------------\n")
print(mngrA.getFirstName(), mngrA.getLastName(), mngrA.computeSalary())
print(mngrB.getFirstName(), mngrB.getLastName(), mngrB.computeSalary())
print(mngrC.getFirstName(), mngrC.getLastName(), mngrC.computeSalary())
print(emplyA.getFirstName(), emplyA.getLastName(), emplyA.computeSalary())
print(emplyB.getFirstName(), emplyB.getLastName(), emplyB.computeSalary())


# In[ ]:




