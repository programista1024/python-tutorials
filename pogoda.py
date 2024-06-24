
# Program generuje prognozę pogody dla Twojej lokalizacji

print("Dzień dobry. Oto prognoza pogody dla Twojej miejscowości na dzisiejszy dzień.")

opis_dnia = "przeważnie pochmurny"
przelotny_deszcz = True
temperatura_dzien = 25 # stopnie Celsjusza
sila_wiatru = "słaby"
predkosc_wiatru = 10 # km/h
wiatr_kierunek = "zachodni"

opis_pogody = f"Spodziewamy się {opis_dnia} dnia"
if przelotny_deszcz:
   opis_pogody += ", z możliwymi przelotnymi opadami deszczu."
else:
   opis_pogody += "."
opis_pogody += f" Temperatura w ciągu dnia osiągnie około {temperatura_dzien} stopni Celsjusza."
opis_pogody += f" Wiatr będzie {sila_wiatru}, z kierunku {wiatr_kierunek}, o prędkości około {predkosc_wiatru} km/h."

print(opis_pogody)
