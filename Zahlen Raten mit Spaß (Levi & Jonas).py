zahl = 673
gerateneZahl = int(input('Rate eine Zahl (0 - 1000): '))
richtig = False
versuche = 0

while richtig == False and versuche < 9:
    versuche += 1
    
    if gerateneZahl == zahl:
        print('Richtig. Versuche: ', versuche)
        richtig = True
    else:
        if gerateneZahl > zahl:
            print('Niedriger')
        if gerateneZahl < zahl:
            print('Höher')
            
        gerateneZahl = int(input('Rate eine Zahl (0 - 1000): '))
        
if versuche >= 9:
    print('Du hast zu viele Versuche gebraucht')