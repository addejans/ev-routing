from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/route')
def get_route():
    # Get start, end, and car location from the request arguments
    start = request.args.get('start').split(',')
    end = request.args.get('end').split(',')
    car = request.args.get('car').split(',')

    # Convert the coordinates to float
    start = [float(start[0]), float(start[1])]
    end = [float(end[0]), float(end[1])]
    car = [float(car[0]), float(car[1])]

    # Simple route information including car location
    route = {
        'start': start,
        'end': end,
        'car_location': car
    }

    return jsonify(route)


if __name__ == '__main__':
    app.run(debug=True)
