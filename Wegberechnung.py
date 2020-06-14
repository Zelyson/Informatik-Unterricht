# Geschwindigkeit in km/h
geschwindigkeit = float(input('Geschwindigkeit (in km/h): '))

# Weg der während der Reaktion zurückgelegt wird
reaktionsweg = (geschwindigkeit / 10) * 3

# Weg der während dem Bremsen zurückgelegt wird
bremsweg = (geschwindigkeit / 10) ** 2

# Gesamt benötigter Weg um anzuhalten
anhalteweg = reaktionsweg + bremsweg

# Ausgabe
print("Reaktionsweg: " + str(int(reaktionsweg)) + "m")
print("Bremsweg: " + str(int(bremsweg)) + "m")
print("Gesamter Weg: " + str(int(anhalteweg)) + "m")