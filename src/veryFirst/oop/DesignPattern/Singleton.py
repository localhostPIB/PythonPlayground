class Singleton:
    __instance = None
    __f = []

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self

    def add(self, s):
        self.__f.append(s)

    def delete(self):
        self.__f.clear()

    def getList(self):
        return self.__f


s1 = Singleton()
s1.add("Hi")

s2 = Singleton()
s2.add("Hallo")

s2 = Singleton()
s2.add("Hello")

list1 = s1.getList()

print(*list1)
print("Anzahl:",len(list1))

s1.delete()
list0 = s2.getList()

print(*list0)
print("Anzahl:",len(list0))
