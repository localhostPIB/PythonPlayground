from __future__ import annotations
from abc import ABC, abstractmethod

"""
Die Basisklasse Component deklariert gemeinsame Operationen 
sowohl für einfache als auch für komplexe Objekte einer Komposition.
"""


class Component(ABC):
    """
    https://refactoring.guru/design-patterns/composite/python/example
    """
    """
       The base Component class declares common operations for both simple and
       complex objects of a composition.
       """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        """
         Optional kann die Basiskomponente eine Schnittstelle deklarieren für das Setzen und Zugriff auf einen Parent 
         der Komponente in einer Baumstruktur deklarieren.  Sie kann auch eine Standardimplementierung für diese
         Methoden bereitstellen.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    """
     In einigen Fällen wäre es vorteilhaft, die Operationen zur Verwaltung der untergeordneten Komponenten Operationen 
     direkt in der Basiskomponentenklasse zu definieren. Auf diese Weise müssen Sie keine keine konkreten 
     Komponentenklassen für den Client-Code offenlegen, auch nicht während der Objektbaum-Assemblierung. 
     Der Nachteil ist, dass diese Methoden für die die Komponenten der Blattebene leer sind.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        """
        Sie können eine Methode bereitstellen, 
        mit der der Client-Code herausfinden kann, ob eine Komponente Kinder haben kann.
        """
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        """
        Die Basiskomponente kann ein Standardverhalten implementieren oder es den konkreten Klassen überlassen 
        (durch Deklaration der Methode, die das Verhalten enthält, als "abstrakt").
        """

        pass
