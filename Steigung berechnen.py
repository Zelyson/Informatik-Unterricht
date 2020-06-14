# Erster Punkt (Eingabe)
p1 = input('Erster Punkt (x, y): ')

# Zweiter Punkt (Eingabe)
p2 = input('Zweiter Punkt (x, y): ')

# Erster Punkt (Koordinaten)
x1 = float(p1.split(", ")[0].replace('(', ''))
y1 = float(p1.split(", ")[1].replace(')', ''))

# Zweiter Punkt (Koordinaten)
x2 = float(p2.split(", ")[0].replace('(', ''))
y2 = float(p2.split(", ")[1].replace(')', ''))

# Steigung berechnen
m = (y2 - y1) / (x2 - x1)

print("Steigung: " + str(m))