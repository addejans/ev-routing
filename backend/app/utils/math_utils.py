import math


def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)


def calculate_charging_time(battery_left, charging_speed):
    battery_needed = 100 - battery_left
    return battery_needed / charging_speed  # time in hours
