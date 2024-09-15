from app.utils.math_utils import calculate_distance, calculate_charging_time
from app.models.route import charging_stations

def plan_route_with_charging(start, end, battery_range, speed=60):
    current_battery = battery_range
    current_location = start
    route = []
    total_distance = calculate_distance(start, end)

    while total_distance > 0:
        next_leg_distance = min(total_distance, current_battery)
        total_distance -= next_leg_distance
        current_battery -= next_leg_distance

        travel_time_hours = next_leg_distance / speed

        if current_battery <= 0 or total_distance > 0:
            nearest_station = min(charging_stations, key=lambda station: calculate_distance(current_location, station['location']))
            station_distance = calculate_distance(current_location, nearest_station['location'])

            if station_distance > current_battery:
                return {"error": "Cannot reach nearest charging station."}

            charging_time = calculate_charging_time(current_battery, nearest_station['charging_speed'])

            route.append({
                'location': nearest_station['location'],
                'action': 'Charge',
                'type': nearest_station['type'],
                'distance_to_next': station_distance,
                'charging_time_hours': charging_time
            })

            current_battery = battery_range
            current_location = nearest_station['location']

        route.append({
            'location': end if total_distance <= 0 else current_location,
            'action': 'Drive',
            'distance_to_next': next_leg_distance,
            'speed': speed,
            'travel_time_hours': travel_time_hours
        })

    return route
