from __future__ import annotations
from Composite import Composite
from Component import Component
from Leaf import Leaf

"""
Der Client-Code arbeitet mit allen Komponenten über die Basisschnittstelle.
"""
"""
  https://refactoring.guru/design-patterns/composite/python/example
 """


def client_code(component: Component) -> None:
    """
        The client code works with all of the components via the base interface.
        """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
        Thanks to the fact that the child-management operations are declared in the
        base Component class, the client code can work with any component, simple or
        complex, without depending on their concrete classes.
        """
    """
        Dank der Tatsache,  dass die Operationen zur Verwaltung der untergeordneten Komponenten 
        in der Basisklasse "Component"  deklariert sind, kann der Client-Code mit jeder beliebigen Komponente,
        ob einfach oder komplex, arbeiten, ohne von ihren konkreten Klassen abhängig zu sein.
        """
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    print("Start")
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
