from abc import ABC, abstractmethod

class employee(ABC):
    def emp_id(self, id, name, salary):
        pass

class childemployee1(employee):
    def emp_id(self, id):
        print("emp_id is 12345")
emp1 = childemployee1()
emp1.emp_id(id)
