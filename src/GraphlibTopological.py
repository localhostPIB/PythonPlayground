import unittest
from graphlib import TopologicalSorter, CycleError

ts = TopologicalSorter()


class Skill:
    def __init__(self, name, skill1):
        self.name = name
        self.skill1 = skill1
        

def topo(liste: list):
    try:
        for i in liste:
            ts.add(i.name, i.skill1)

        
        x = tuple(ts.static_order()) # Raise CycleError
        print(x)
    except CycleError as ce:
        raise ce
        
        
 class GraphTest(unittest.TestCase):
    def test(self):
        list = []
        skill1 = Skill("Prog. 1", "Roboter bedienen")
        skill2 = Skill("Roboter proggen", "Roboter bauen")
        skill3 = Skill("Roboter bauen", "Roboter bedienen")
        skill4 = Skill("Roboter bedienen", "Prog. 1")
        list.append(skill1)
        list.append(skill2)
        list.append(skill3)
        list.append(skill4)
        topo(list)       
        
