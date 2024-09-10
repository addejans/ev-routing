# **EV Routing Project**

## **Table of Contents**
- [Overview](#overview)
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
- [Demo](#demo)

## **Overview**
This project simulates the routing of electric vehicles (EVs) from one point to another, considering key factors like battery consumption, charging stations, and road networks. The frontend uses **Leaflet.js** for map visualization, and the backend is powered by **Python** (Flask or FastAPI) to handle routing algorithms, battery simulation, and more.

The project is developed iteratively, starting with simple point-to-point navigation and expanding to include dynamic routing, charging station management, and real-time EV data.

## **Features**
1. **Basic EV Routing**: The initial version allows a user to select a starting point (Point A) and a destination (Point B) on a map, and visualize the route between them.
2. **Battery Simulation**: The system calculates battery usage as the EV travels between points.
3. **Charging Stations**: Routing algorithms include charging stations, allowing the EV to recharge during long trips.
4. **Dynamic Mapping**: Integration with real-world road networks using the Leaflet.js and OpenStreetMap API.
5. **Multiple EV Simulation (Planned)**: Future versions will simulate multiple EVs sharing the same grid, interacting with charging stations in real time.

## **Tech Stack**
- **Frontend**: 
  - [Leaflet.js](https://leafletjs.com/) for interactive maps and route visualization.
  - HTML, CSS, JavaScript.
- **Backend**: 
  - [Python](https://www.python.org/) for server-side logic.
  - [Flask](https://flask.palletsprojects.com/) or [FastAPI](https://fastapi.tiangolo.com/) to handle API requests.
- **Mapping API**: 
  - [OpenStreetMap](https://www.openstreetmap.org/) for real-world road networks.
  
## **Project Structure**
```
ev-routing-project/
│
├── backend/                # Python backend code
│   ├── app.py              # Main backend server file
│   ├── routes.py           # API routes for routing logic
│   ├── battery.py          # Battery consumption and energy logic
│   ├── charging.py         # Charging station management
│   ├── requirements.txt    # Backend dependencies
│
├── frontend/               # Frontend code (Leaflet.js, HTML, CSS)
│   ├── index.html          # Main UI with Leaflet.js
│   ├── map.js              # JS logic for Leaflet maps and API calls
│   └── styles.css          # Styling for the UI
│
├── tests/                  # Tests for both frontend and backend
│   ├── backend/            # Backend-specific tests
│   ├── frontend/           # Frontend-specific tests (e.g., JS unit tests)
│
└── README.md               # Project documentation
```

## **Installation**

### **Backend Setup**
1. Clone the repository and navigate to the `backend` directory.
   ```bash
   git clone <repo-url>
   cd ev-routing-project/backend
   ```

2. Create a virtual environment and install dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the Flask server (or FastAPI).
   ```bash
   python app.py  # For Flask
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
2. The backend will calculate a simple route between the two points.
3. The EV will move between the points and simulate battery consumption.
4. As new features are added, you will be able to:
   - Include charging stations in the route.
   - View battery levels over time.
   - Simulate multiple EVs using the same charging grid.

## **Roadmap**
The project will be developed iteratively, with the following planned features:
1. **Phase 1**: Basic point-to-point EV routing with straight-line navigation. *(In Progress)*
2. **Phase 2**: Battery consumption simulation based on distance traveled. *(Not started)*
3. **Phase 3**: Integration of charging stations and charging behavior. *(Not started)*
4. **Phase 4**: Use of real-world road networks via OpenStreetMap. *(Not started)*
5. **Phase 5**: Simulating multiple EVs and interactions with the charging grid. *(Not started)*
6. **Phase 6**: Adding probabilistic failure models for charging stations. *(Not started)*

## **Contributing**
If you'd like to contribute to this project, feel free to submit issues or pull requests! We welcome ideas for new features, improvements to the routing algorithms, and code optimizations.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **API Documentation**

The backend provides several endpoints for interacting with the EV routing system. Below are the detailed descriptions of each endpoint:

### **1. `/route`**

- **Method**: `GET`
- **Description**: Calculates a route from a starting point (A) to a destination (B). Currently, the route is a simple straight line, but future iterations will include road networks and optimized routing with charging stations.
- **Endpoint**: `/route?start=<latitude,longitude>&end=<latitude,longitude>`
  
#### **Request Parameters**:
- `start`: The starting point of the route, represented as `latitude,longitude`.
- `end`: The destination point, represented as `latitude,longitude`.

#### **Example Request**:
```bash
GET /route?start=37.7749,-122.4194&end=34.0522,-118.2437
```

#### **Response**:
- **200 OK**: Returns the route details as a JSON object with the start and end points.
  
#### **Response Example**:
```json
{
  "start": [37.7749, -122.4194],
  "end": [34.0522, -118.2437],
  "route": [[37.7749, -122.4194], [36.7783, -119.4179], [34.0522, -118.2437]]
}
```

---

### **2. `/battery-status`**

- **Method**: `GET`
- **Description**: Calculates the remaining battery level for the EV after traveling a specified distance. The battery consumption is based on a fixed rate of energy usage per mile.
- **Endpoint**: `/battery-status?distance=<distance>`

#### **Request Parameters**:
- `distance`: The distance traveled by the EV in miles.

#### **Example Request**:
```bash
GET /battery-status?distance=200
```

#### **Response**:
- **200 OK**: Returns the remaining battery percentage after traveling the specified distance.
  
#### **Response Example**:
```json
{
  "initial_battery": 100,
  "distance_traveled": 200,
  "battery_remaining": 60
}
```

---

### **3. `/charging-stations`**

- **Method**: `GET`
- **Description**: Provides a list of available charging stations along the route. The stations include details like location, type (fast/slow charger), and estimated charging time.
- **Endpoint**: `/charging-stations?route=<start_latitude,start_longitude,end_latitude,end_longitude>`

#### **Request Parameters**:
- `route`: The start and end points of the trip, represented as `start_latitude,start_longitude,end_latitude,end_longitude`. The backend will calculate which charging stations fall along this route.

#### **Example Request**:
```bash
GET /charging-stations?route=37.7749,-122.4194,34.0522,-118.2437
```

#### **Response**:
- **200 OK**: Returns a list of charging stations available along the route.
  
#### **Response Example**:
```json
{
  "charging_stations": [
    {
      "station_id": 1,
      "location": [36.7783, -119.4179],
      "type": "fast",
      "estimated_charging_time": 30
    },
    {
      "station_id": 2,
      "location": [35.3733, -119.0187],
      "type": "slow",
      "estimated_charging_time": 120
    }
  ]
}
```

## **Demo**

**Demo Link**: *(URL to go here)*
