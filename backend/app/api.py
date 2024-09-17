from flask import Blueprint, request, jsonify
from app.services.route_service import plan_route_with_charging

route_blueprint = Blueprint("route_blueprint", __name__)


@route_blueprint.route("/route", methods=["GET"])
def get_route():
    # Get start, end locations, and optional battery range from the request arguments
    start = request.args.get("start").split(",")
    end = request.args.get("end").split(",")
    battery_range = float(
        request.args.get("battery_range", 100)
    )  # Default range of 100 miles

    # Convert the coordinates to float
    start = [float(start[0]), float(start[1])]
    end = [float(end[0]), float(end[1])]

    # Plan route using the route_service logic
    planned_route = plan_route_with_charging(start, end, battery_range)

    # Return the start, end, and waypoints with charging stops if needed
    return jsonify({"start": start, "end": end, "route": planned_route})
