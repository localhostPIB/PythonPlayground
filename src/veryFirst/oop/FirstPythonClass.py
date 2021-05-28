class FirstPythonClass():
    """Erste Klasse in Python"""

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.test = 0

    def tue_was(self, name, anzahl=1):
        print("was getan ? ", anzahl*name)


teste0 = FirstPythonClass("Oliver", 28)
teste0.tue_was(teste0.name, 3)
