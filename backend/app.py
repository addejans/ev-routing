from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/route')
def get_route():
    start = request.args.get('start').split(',')
    end = request.args.get('end').split(',')
    start = [float(start[0]), float(start[1])]
    end = [float(end[0]), float(end[1])]
    
    # Simple straight-line route for now
    route = {
        'start': start,
        'end': end
    }
    return jsonify(route)

if __name__ == '__main__':
    app.run(debug=True)

