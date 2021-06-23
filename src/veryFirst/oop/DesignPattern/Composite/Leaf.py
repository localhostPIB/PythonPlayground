from __future__ import annotations
from Component import Component

"""
Die Klasse Leaf repräsentiert die Endobjekte einer Komposition. Ein Blatt kann keine Kinder haben.
Normalerweise sind es die Leaf-Objekte, die die eigentliche Arbeit machen, während Composite Objekte 
nur an ihre Unterkomponenten delegieren.
"""


class Leaf(Component):
    """
      https://refactoring.guru/design-patterns/composite/python/example
    """

    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def operation(self) -> str:
        return "Leaf"
