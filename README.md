# **EV Routing Project**

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
1. **Phase 1**: Basic point-to-point EV routing with straight-line navigation. *(Complete)*
2. **Phase 2**: Battery consumption simulation based on distance traveled.
3. **Phase 3**: Integration of charging stations and charging behavior.
4. **Phase 4**: Use of real-world road networks via OpenStreetMap.
5. **Phase 5**: Simulating multiple EVs and interactions with the charging grid.
6. **Phase 6**: Adding probabilistic failure models for charging stations.

## **Contributing**
If you'd like to contribute to this project, feel free to submit issues or pull requests! We welcome ideas for new features, improvements to the routing algorithms, and code optimizations.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Additional Sections for Future**:
- **API Documentation**: As your API grows, you can add detailed explanations of each endpoint, including `/route`, `/battery-status`, `/charging-stations`.
- **Demo Link**: If you host a demo version of the app, add the URL here.
