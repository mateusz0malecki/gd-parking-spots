from django.db import models


parking_lots_map = {
    "1": "Galeria Bałtycka",
    "2": "C.H. Manhattan",
    "3": "PGE Arena",
    "4": "AmberExpo",
    "5": "C.H. Madison",
    "7": "Akademia Muzyczna",
    "14": "Europejskie Centrum Solidarności",
    "15": "CH Metropolia",
    "17": "Forum Gdańsk",
    "18": "Parking Błękitna",
    "19": "Parking Kapliczna",
    "20": "Parking Kaczyńskiego",
    "21": "Parking Czarny Dwór",
    "22": "Parking Świętokrzyska",
}


class ParkingSpot(models.Model):
    parking_id = models.CharField(max_length=100, unique=True)
    parking_name = models.CharField(max_length=255)
    available_spots = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
