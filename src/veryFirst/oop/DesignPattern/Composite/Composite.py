from __future__ import annotations
from Component import Component
from typing import List

""" 
Die Klasse Composite repräsentiert die komplexen Komponenten, die Kinder haben können. Normalerweise delegieren 
die Composite-Objekte die eigentliche Arbeit an ihre Kinder und "summieren" dann das Ergebnis auf.
"""


class Composite(Component):
    """
      https://refactoring.guru/design-patterns/composite/python/example
      """
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    """
    Ein zusammengesetztes Objekt kann andere Komponenten (sowohl einfache als auch komplexe) zu seiner untergeordneten 
    Liste hinzufügen oder daraus entfernen. komplex) zu seiner untergeordneten Liste hinzufügen oder daraus entfernen.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        """
        Das Composite führt seine primäre Logik auf eine bestimmte Weise aus. Es durchläuft rekursiv alle seine 
        untergeordneten Elemente und sammelt und summiert deren Ergebnisse. Da die Kinder des Composites diese 
        Aufrufe an ihre Kinder und so weiter weitergeben, wird als Ergebnis der gesamte Objektbaum durchlaufen.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
