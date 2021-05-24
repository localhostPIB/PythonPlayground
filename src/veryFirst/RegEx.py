import re


def regExDelux():
    plz = "66111,78250, Hallo, Welt"
    email = "max_mustermann@web.de"
    url = 'www.google.de'
    cc = '1234 5678 0000 1222'
    svn = "12 123456 L 92 3, 34 898222 K 98 3"

    regExCc = r'^(\d{4}\s*){4}'
    regExEmail = r'^([\w\.\-]+)@([\w\-]+)((\.(\w){2,})+)$'
    regExPlz = r'\d{5}'
    regExUrl = r'^(http:|https:|www\.)*\S+'
    regExSVN = r'^(\d{2})\s(\d{6})\s\D\s\d{2}\s\d{1}'

    pattern = re.compile(regExPlz)
    print(pattern.findall(plz))

    pattern = re.compile(regExEmail)
    print(pattern.findall(email))

    pattern = re.compile(regExUrl)
    print(pattern.search(url))

    pattern = re.compile(regExCc)
    print(pattern.search(cc))

    pattern = re.compile(regExSVN)
    liste = [[m.start(), m.end(), m.group()] for m in pattern.finditer(svn)]
    print(liste)


class Zeichenkette():
    def extraktion(self):
        regExEmail = r'^([\w\.\-]+)@([\w\-]+)((\.(\w){2,})+)'
        regExTel = r'\d{4}\D\d{,99}'
        patternTel = re.compile(regExTel)
        patternEmail = re.compile(regExEmail)
        liste = [[m.group()] for m in patternTel.finditer(self)]
        liste.append([n.group() for n in patternEmail.finditer(self)])
        print(liste)

    def whiteSpaceKiller(self):
        regExWS = r'\x20{2,}'
        regExSZ = r'[.!?\\-]'
        regExWW = r'(?si)\b(\w+)\b(?=.*?\b\1\b)'
        patternWS = re.compile(regExWS)
        patternSZ = re.compile(regExSZ)
        patternWW = re.compile(regExWW)
        s = patternWS.sub(" ", self)
        s1 = patternSZ.sub("", s)
        result = patternWW.sub("", s1)

        print(result)


zk0 = 'Hallo@welt.de 0681/000000 Pikachu pika pika'
zk1 = "Hallo Welt Welt"
Zeichenkette.whiteSpaceKiller(zk1)
