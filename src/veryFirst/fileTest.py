datei = open('test.py', 'r+')

print("Inhalt aus Datei: ")

for zeile in datei:
    print(zeile)


datei.write("weitere Zeile")

datei.close()
