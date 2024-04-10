
bob = {
    "name": "Bob",
    "id": 481723904,
    "role": "intern"
}

anne = {
    "name": "Anne",
    "id": 4877428789,
    "role": "Manager"
}

print(bob["name"], bob["id"], bob["role"])

print(anne["name"], anne["id"], anne["role"])

def employee_print(e):
    print(e["name"], e["id"], e["role"])

employee_print(bob)
employee_print(anne)

def employee_make(name, id, role):
    return {
    "name": name,
    "id": id,
    "role": role
}

eoin = employee_make("Eoin", 3823, "CEO")

employee_print(eoin)

bob["role"] = "fulltime"

def employee_set_role(e, new_role):
    # validate new_role
    e["role"] = new_role

employee_set_role(bob, "fulltime")
employee_print(bob)

class Employee:
    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.role = role
        self.old_role = ""

    def print(self):
        print(self.name, self.id, self.role)

    def set_role(self, new_role):
        # validate
        self.old_role = self.role
        self.role = new_role

rob = Employee("Rob", 492749872, "CTO")

rob.print()

rob.set_role("Manager")
rob.print()