class Visitor:
    def visit_element_a(self, element_a):
        pass

    def visit_element_b(self, element_b):
        pass


class ConcreteVisitor1(Visitor):
    def visit_element_a(self, element_a):
        print(f"ConcreteVisitor1 visit {element_a}")

    def visit_element_b(self, element_b):
        print(f"ConcreteVisitor1 visit {element_b}")


class ConcreteVisitor2(Visitor):
    def visit_element_a(self, element_a):
        print(f"ConcreteVisitor2 visit {element_a}")

    def visit_element_b(self, element_b):
        print(f"ConcreteVisitor2 visit {element_b}")


class ElementInterface:
    def accept(self, visitor: Visitor):
        pass


class ElementA(ElementInterface):
    def methodA(self):
        pass

    def accept(self, visitor: Visitor):
        visitor.visit_element_a(self)


class ElementB(ElementInterface):
    def methodB(self):
        pass

    def accept(self, visitor: Visitor):
        visitor.visit_element_b(self)
