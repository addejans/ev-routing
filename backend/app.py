from flask import Flask, request, jsonify
import random
import math

app = Flask(__name__)

# Simulated list of charging station locations (latitude, longitude, type, and charging speed)
charging_stations = [
    {'location': [34.05, -118.25], 'type': 'Fast Charger', 'charging_speed': 120},  # Example: Los Angeles
    {'location': [36.16, -115.15], 'type': 'Regular Charger', 'charging_speed': 50},  # Example: Las Vegas
    {'location': [37.77, -122.41], 'type': 'Fast Charger', 'charging_speed': 120},  # Example: San Francisco
    {'location': [35.68, -105.94], 'type': 'Regular Charger', 'charging_speed': 50},  # Example: Santa Fe
]

# Function to calculate the Euclidean distance (simplified for demo purposes)
def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

# Function to calculate charging time based on battery level and charging speed
def calculate_charging_time(battery_left, charging_speed):
    # Assume battery capacity of 100 kWh, and calculate how much needs to be charged
    battery_needed = 100 - battery_left
    # Charging time = battery needed (kWh) / charging speed (kW)
    return battery_needed / charging_speed  # time in hours

# Function to determine if a charging stop is needed based on battery capacity and distance
def plan_route_with_charging(start, end, battery_range, stations, speed=60):
    current_battery = battery_range
    current_location = start
    route = []
    total_distance = calculate_distance(start, end)

    # Simulate movement toward the destination
    while total_distance > 0:
        next_leg_distance = min(total_distance, current_battery)
        total_distance -= next_leg_distance
        current_battery -= next_leg_distance

        # Time to travel to the next waypoint or charging stop
        travel_time_hours = next_leg_distance / speed

        # Check if battery will run out before reaching the destination
        if current_battery <= 0 or total_distance > 0:
            # Find the nearest charging station
            nearest_station = min(stations, key=lambda station: calculate_distance(current_location, station['location']))
            station_distance = calculate_distance(current_location, nearest_station['location'])

            if station_distance > current_battery:
                # Not enough battery to reach the nearest charging station
                return {"error": "Cannot reach nearest charging station."}

            # Calculate charging time based on battery level and charging station speed
            charging_time = calculate_charging_time(current_battery, nearest_station['charging_speed'])

            # Add the charging stop to the route
            route.append({
                'location': nearest_station['location'],
                'action': 'Charge',
                'type': nearest_station['type'],
                'distance_to_next': station_distance,
                'charging_time_hours': charging_time  # Time in hours
            })

            # Recharge the battery
            current_battery = battery_range

            # Update current location to the charging station
            current_location = nearest_station['location']

        # Continue to the next leg of the journey or destination
        route.append({
            'location': end if total_distance <= 0 else current_location,
            'action': 'Drive',
            'distance_to_next': next_leg_distance,
            'speed': speed,  # Reintroducing speed in driving legs
            'travel_time_hours': travel_time_hours  # Time to travel this segment
        })

    print(route)

    return route

@app.route('/route')
def get_route():
    # Get start, end locations, and optional battery range from the request arguments
    start = request.args.get('start').split(',')
    end = request.args.get('end').split(',')
    battery_range = float(request.args.get('battery_range', 100))  # Default range of 100 miles

    # Convert the coordinates to float
    start = [float(start[0]), float(start[1])]
    end = [float(end[0]), float(end[1])]

    # Plan route with charging stops based on the start, end, and battery range
    planned_route = plan_route_with_charging(start, end, battery_range, charging_stations, speed=60)  # Constant speed of 60 mph

    # Return the start, end, and waypoints with charging stops if needed
    response = {
        'start': start,
        'end': end,
        'route': planned_route
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
