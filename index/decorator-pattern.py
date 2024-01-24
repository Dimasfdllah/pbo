class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        self._component.operation()

class ConcreteDecorator(Decorator):
    def operation(self):
        super().operation()
        print("ConcreteDecorator operation")

# Client Code
component = ConcreteComponent()
decorator = ConcreteDecorator(component)
decorator.operation()  # Output: ConcreteComponent operation, ConcreteDecorator operation
