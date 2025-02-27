from geopy.distance import geodesic
import random
import time

def get_gps_coordinates():
    """Simule l'acquisition des coordonnées GPS de la vache."""
    # Remplacez ces coordonnées par celles de votre ferme
    base_lat, base_lon = 48.8566, 2.3522  # Exemple : Paris
    
    # Simule des variations autour de la position de référence
    lat = base_lat + random.uniform(-0.0001, 0.0001)
    lon = base_lon + random.uniform(-0.0001, 0.0001)
    
    return lat, lon

def calculate_distance(coord_vache, coord_porte):
    """Calcule la distance entre la vache et la porte de la ferme en mètres."""
    return geodesic(coord_vache, coord_porte).meters

def monitor_cow():
    """Surveille la position de la vache et déclenche une alerte si elle s'éloigne de plus de 5m."""
    # Coordonnées de la porte de la ferme (exemple)
    porte_lat, porte_lon = 48.8566, 2.3522
    coord_porte = (porte_lat, porte_lon)
    
    while True:
        coord_vache = get_gps_coordinates()
        distance = calculate_distance(coord_vache, coord_porte)
        print(f"Distance actuelle : {distance:.2f} mètres")
        
        if abs(distance) > 5:
            print("⚠️ ALERTE : La vache s'est trop éloignée de la ferme !")
        
        time.sleep(2)  # Vérification toutes les 2 secondes

if __name__ == "__main__":
    monitor_cow()
