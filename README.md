Here’s an updated version of the README to reflect the latest API structure and changes:

---

# **EV Routing**

## **Table of Contents**
- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [API Documentation](#api-documentation)

## **Overview**
This project simulates the routing of electric vehicles (EVs) from one point to another, considering key factors like battery consumption, charging stations, and road networks. The frontend uses **Leaflet.js** for map visualization, and the backend is powered by **Python** (Flask) to handle routing algorithms, battery simulation, charging station management, and more.

The project is being developed iteratively, starting with simple point-to-point navigation and expanding to include dynamic routing, charging station management, and real-time EV data.

## **Demo**

**Demo Link**: *(URL to go here)*

**Screenshots**:

*(Insert demo screenshots here)*

## **Features**
1. **EV Routing with Battery Simulation**: The backend calculates a route between two points, simulating battery consumption and incorporating charging stations when needed.
2. **Charging Station Management**: The system selects charging stations along the route when the battery is insufficient to complete the journey.
3. **Charging Time Calculation**: Charging time at each stop is calculated based on the charging station type (fast/regular) and the remaining battery level.
4. **Real-time Route Updates**: The route dynamically updates with charging stops and battery level changes.
5. **Dynamic Mapping**: Frontend uses **Leaflet.js** to provide a visual route map.

## **Tech Stack**
- **Frontend**: 
  - [Leaflet.js](https://leafletjs.com/) for interactive maps and route visualization.
  - HTML, CSS, JavaScript.
- **Backend**: 
  - [Python](https://www.python.org/) for server-side logic.
  - [Flask](https://flask.palletsprojects.com/) for handling API requests.
  
## **Project Structure**
```
ev-routing/
│
├── /app/                   # Python backend application
│   ├── __init__.py          # Initializes Flask app and imports routes
│   ├── api.py               # Defines the HTTP API endpoints
│   ├── /services            # Contains business logic for route planning
│   │   └── route_service.py  # Logic for battery management and routing
│   ├── /models              # Data models
│   │   └── route.py          # Charging station data
│   ├── /utils               # Utility functions
│   │   └── math_utils.py     # Distance calculations and battery usage
│   └── requirements.txt     # Backend dependencies
│
├── frontend/                # Frontend code (Leaflet.js, HTML, CSS)
│   ├── index.html           # Main UI with Leaflet.js
│   ├── map.js               # JavaScript logic for frontend
│   └── styles.css           # Frontend styling
│
└── README.md                # Project documentation
```

## **Installation**

### **Backend Setup**
1. Clone the repository and navigate to the `app` directory.
   ```bash
   git clone <repo-url>
   cd ev-routing/app
   ```

2. Create a virtual environment and install dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the Flask server.
   ```bash
   python app.py
   ```

4. The backend will run on `http://127.0.0.1:5000`.

### **Frontend Setup**
1. Navigate to the `frontend` directory.
   ```bash
   cd ../frontend
   ```

2. Open the `index.html` file in your browser or run a local server.
   - If you’re using Python, you can run a simple HTTP server:
     ```bash
     python -m http.server 8000
     ```

3. The frontend will be available at `http://localhost:8000`.

## **Usage**
1. Open the frontend (browser) and select **Point A** and **Point B** by clicking on the map.
2. The backend will calculate a route between the two points, including charging stops if necessary.
3. The EV will move between the points and simulate battery consumption.
4. As new features are added, you will be able to:
   - Include charging stations in the route.
   - View battery levels over time.
   - Simulate charging times at charging stations.

## **Roadmap**
The project will be developed iteratively, with the following planned features:
1. **Phase 1**: Basic point-to-point EV routing with straight-line navigation. *(In Progress)*
2. **Phase 2**: Displaying metrics on the front-end (e.g., travel-time, travel-distance, battery-usage) *(Not started)*
3. **Phase 3**: Battery consumption simulation based on distance traveled. *(Not started)*
4. **Phase 4**: Integration of charging stations and charging behavior. *(Not started)*
5. **Phase 5**: Use of real-world road networks via OpenStreetMap. *(Not started)*
6. **Phase 6**: Simulating multiple EVs and interactions with the charging grid. *(Not started)*
7. **Phase 7**: Adding probabilistic failure models for charging stations. *(Not started)*

## **Contributing**
If you'd like to contribute to this project, feel free to submit issues or pull requests! We welcome ideas for new features, improvements to the routing algorithms, and code optimizations.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **API Documentation**

The backend provides several endpoints for interacting with the EV routing system:

### **1. `/route`**

- **Method**: `GET`
- **Description**: Calculates a route from a starting point to a destination, incorporating charging stations if necessary.
- **Endpoint**: `/route?start=<latitude,longitude>&end=<latitude,longitude>&battery_range=<battery_range>`
  
#### **Request Parameters**:
- `start`: The starting point of the route, represented as `latitude,longitude`.
- `end`: The destination point, represented as `latitude,longitude`.
- `battery_range`: Optional parameter, representing the EV's battery range in miles (default: 100 miles).

#### **Example Request**:
```bash
GET /route?start=37.7749,-122.4194&end=34.0522,-118.2437&battery_range=100
```

#### **Response**:
- **200 OK**: Returns the route details, including any charging stops.

#### **Response Example**:
```json
{
  "start": [37.7749, -122.4194],
  "end": [34.0522, -118.2437],
  "route": [
    {
      "location": [37.7749, -122.4194],
      "action": "Drive",
      "distance_to_next": 100.0,
      "speed": 60,
      "travel_time_hours": 1.6667
    },
    {
      "location": [36.16, -115.15],
      "action": "Charge",
      "type": "Regular Charger",
      "distance_to_next": 50.0,
      "charging_time_hours": 1.0
    },
    {
      "location": [34.0522, -118.2437],
      "action": "Drive",
      "distance_to_next": 150.0,
      "speed": 60,
      "travel_time_hours": 2.5
    }
  ]
}
```

---

