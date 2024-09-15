from app.utils.math_utils import calculate_distance, calculate_charging_time
from app.models.route import charging_stations


def plan_route_with_charging(start, end, battery_range, speed=60):
    """
    Plan a route for an electric vehicle (EV) from a starting point to an endpoint, considering battery range
    and charging stations along the way. If the battery is insufficient to reach the destination, the route will
    include stops at the nearest charging stations.

    Parameters:
    -----------
    start : list
        Starting point of the journey in the form [latitude, longitude].
    end : list
        Destination point of the journey in the form [latitude, longitude].
    battery_range : float
        The distance (in miles) that the EV can travel on a full battery charge.
    speed : float, optional
        Speed of the vehicle in miles per hour (default is 60 mph).

    Returns:
    --------
    route : list
        A list of route segments (driving and charging), where each segment contains the following keys:
        - 'location': Coordinates of the point (start, charging station, or end).
        - 'action': 'Drive' for driving segments and 'Charge' for charging stops.
        - 'distance_to_next': Distance to the next point in the route.
        - 'speed': Driving speed in mph (only for driving segments).
        - 'travel_time_hours': Time taken for the driving segment in hours.
        - 'charging_time_hours': Charging time in hours (only for charging segments).
    """

    current_battery = battery_range  # Initialize the battery to the full range
    current_location = start  # Set the current location to the start point
    route = []  # Initialize the route list
    total_distance = calculate_distance(
        start, end
    )  # Calculate the total distance between start and end points

    # Keep iterating while there is remaining distance to the destination
    while total_distance > 0:
        # Calculate the distance for the next leg of the journey (either to the destination or as far as the battery allows)
        next_leg_distance = min(total_distance, current_battery)

        # Reduce the remaining total distance and battery range accordingly
        total_distance -= next_leg_distance
        current_battery -= next_leg_distance

        # Calculate travel time based on speed
        travel_time_hours = next_leg_distance / speed

        # Check if the vehicle needs to stop for charging
        if current_battery <= 0 or total_distance > 0:
            # Find the nearest charging station from the current location
            nearest_station = min(
                charging_stations,
                key=lambda station: calculate_distance(
                    current_location, station["location"]
                ),
            )
            station_distance = calculate_distance(
                current_location, nearest_station["location"]
            )

            # If the nearest charging station is too far to reach, return an error
            if station_distance > current_battery:
                return {"error": "Cannot reach nearest charging station."}

            # Calculate how long it will take to charge the battery at this station
            charging_time = calculate_charging_time(
                current_battery, nearest_station["charging_speed"]
            )

            # Add a charging stop to the route
            route.append(
                {
                    "location": nearest_station[
                        "location"
                    ],  # Location of the charging station
                    "action": "Charge",  # Action: charging stop
                    "type": nearest_station[
                        "type"
                    ],  # Type of charging station (e.g., Fast or Regular)
                    "distance_to_next": station_distance,  # Distance from the current location to the charging station
                    "charging_time_hours": charging_time,  # Charging time required at the station
                }
            )

            # After charging, the battery is full again
            current_battery = battery_range

            # Update the current location to the charging station
            current_location = nearest_station["location"]

        # Append the driving segment (whether to the destination or next leg)
        route.append(
            {
                "location": (
                    end if total_distance <= 0 else current_location
                ),  # If no more distance, set location to 'end'
                "action": "Drive",  # Action: driving
                "distance_to_next": next_leg_distance,  # Distance to the next point
                "speed": speed,  # Speed during this leg
                "travel_time_hours": travel_time_hours,  # Time taken to complete this leg
            }
        )

    return route
