start = 1000
zinsen = 6
betrag = 10
jahresende = 0
jahre = 0

print('Start: ' + str(start) + '€   Zinsen: ' + str(zinsen) + '%   Monatliche Einzahlung: ' + str(betrag) + '€')

while start > 0:
    zusatz = (start * zinsen) / 100
    jahresende = start - zusatz
    start = jahresende
    jahre = jahre + 1
    
print(str(jahre))