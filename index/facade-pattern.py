class SubsystemA:
    def operation_a(self):
        print("Subsystem A operation")

class SubsystemB:
    def operation_b(self):
        print("Subsystem B operation")

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()

# Client Code
facade = Facade()
facade.operation()  # Output: Subsystem A operation, Subsystem B operation
