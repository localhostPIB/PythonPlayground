import random

lottozahlen_alle = []
lottozahlen_gewinner = random.sample(range(1, 50), 6)
print(lottozahlen_gewinner)


#lottozahlen_alle = []
#lottozahlen_alle.extend(range(1, 50))
#lottozahlen_gewinner = random.sample(lottozahlen_alle, 6)
#lottozahlen_gewinner.sort()
#print(lottozahlen_gewinner)
