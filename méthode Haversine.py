import math

# Fonction pour calculer la distance en mètres entre deux points GPS
def haversine(lat1, lon1, lat2, lon2):
    # Rayon de la Terre en mètres
    R = 6371000

    # Conversion des coordonnées en radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Formule de Haversine
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance en mètres
    distance = R * c
    return distance

# Coordonnées GPS de la vache (latitude, longitude)
lat_vache = float(input("Entrez la latitude de la vache (en degrés) : "))
lon_vache = float(input("Entrez la longitude de la vache (en degrés) : "))

# Coordonnées GPS de la porte de la ferme (latitude, longitude)
lat_porte = float(input("Entrez la latitude de la porte (en degrés) : "))
lon_porte = float(input("Entrez la longitude de la porte (en degrés) : "))

# Calcul de la distance entre la vache et la porte
distance = haversine(lat_vache, lon_vache, lat_porte, lon_porte)

# Alerte si la distance est supérieure ou inférieure à 5 mètres par rapport à la valeur 5
if abs(distance - 5) > 5:
    print(f"Alerte : La distance entre la vache et la porte est de {distance:.2f} mètres, ce qui est en dehors de la plage de ±5 mètres.")
else:
    print(f"La distance entre la vache et la porte est de {distance:.2f} mètres, ce qui est dans la plage acceptable de ±5 mètres.")
