import os
from django.shortcuts import render

from .http_client import aiohttp_client
from .models import ParkingSpot, parking_lots_map


async def index(request):
    response = await aiohttp_client.session.get(os.getenv('GD_URL'))
    parkingspots = await response.json()
    parking_lots = parkingspots.get('parkingLots', [])
    parking_lots = [
        ParkingSpot(
            parking_id=parking_lot.get('parkingId'),
            parking_name=parking_lots_map.get(parking_lot.get('parkingId'), 'Unknown Parking Lot'),
            available_spots=parking_lot.get('availableSpots', 0),
            last_updated=parking_lot.get('lastUpdate', None)
        ) for parking_lot in parking_lots
    ]
    return render(request, 'parkingspots/index.html', {'parking_lots': parking_lots})
