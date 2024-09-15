from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/route')
def get_route():
    # Get start and end locations from the request arguments
    start = request.args.get('start').split(',')
    end = request.args.get('end').split(',')

    # Convert the coordinates to float
    start = [float(start[0]), float(start[1])]
    end = [float(end[0]), float(end[1])]

    # Generate made-up waypoints between start and end, with random speeds
    waypoints = [
        {'location': [start[0] + 1, start[1] + 1], 'speed': random.uniform(30, 70)},
        {'location': [start[0] + 2, start[1] + 2], 'speed': random.uniform(30, 70)},
        {'location': [start[0] + 3, start[1] + 3], 'speed': random.uniform(30, 70)},
        {'location': [end[0] - 1, end[1] - 1], 'speed': random.uniform(30, 70)},
    ]

    # Return the start, end, and waypoints with speed
    route = {
        'start': start,
        'end': end,
        'waypoints': waypoints
    }

    return jsonify(route)

if __name__ == '__main__':
    app.run(debug=True)
