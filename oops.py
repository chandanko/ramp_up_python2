class employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def details(self):
        print(f"name of the employee : {self.name} ")
        print(f"Employee id : {self.emp_id}")

class developer(employee):
    def __init__(self,name,emp_id,programming):
        self.programming=programming
        super().__init__(name,emp_id)
    def details(self):
        super().details()
        print(f"The programming language is : {self.programming}")

class manager(employee):
    def __init__(self,name,emp_id,department):
        self.department=department
        super().__init__(name,emp_id)
    def details(self):
        super().details()
        print(f"The department is : {self.department}")

obj_1=developer("chandan",2979,"python")
obj_2=manager("chandan",2979,"QA")
obj_1.details()
obj_2.details()