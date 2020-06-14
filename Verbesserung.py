# Eingabe
population = float(input('Population zu Beginn: '))

# Verarbeitung
jahr = 2010
while jahr < 2020:
    jahr = jahr + 1
    population = population * 1.05

# Ausgabe
print('Population am Ende: ' + str(population))
