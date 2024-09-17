import React, { useEffect, useState } from 'react';
import { mapNode } from '../types/mapNode';
import { routeData } from '../types/routeData';

const RoutePlanner = ({
  start,
  end,
  batteryRange,
  setStart,
  setEnd,
  setBatteryRange,
}: {
  start: mapNode;
  end: mapNode;
  batteryRange: number;
  setStart: (node: mapNode) => void;
  setEnd: (node: mapNode) => void;
  setBatteryRange: (range: number) => void;
}) => {
  const [route, setRoute] = useState<routeData>({
    location: { latitude: 0, longitude: 0 },
    action: '',
    speed: 0,
    distance_to_next: 0,
    travel_time_hours: 0,
    charging_time_hours: 0,
  }); // For storing the response

  const fetchRoute = async () => {
    try {
      // Construct the URL dynamically using template literals
      const url = `http://127.0.0.1:5000/route?start=${start.latitude},${start.longitude}&end=${end.latitude},${end.longitude}&battery_range=${batteryRange}`;

      // Fetch the route data
      const response = await fetch(url);
      const data = await response.json();

      // Update the state with the response data
      setRoute(data);
    } catch (error) {
      console.error('Error fetching route data:', error);
    }
  };

  useEffect(() => {
    console.log(route);
  }, [route]);

  return (
    <div>
      <h1>EV Route Planner</h1>

      <div>
        <label>Start Latitude:</label>
        <input
          type="number"
          value={start.latitude}
          onChange={(e) =>
            setStart({ ...start, latitude: parseFloat(e.target.value) })
          }
        />

        <label>Start Longitude:</label>
        <input
          type="number"
          value={start.longitude}
          onChange={(e) =>
            setStart({ ...start, longitude: parseFloat(e.target.value) })
          }
        />
      </div>

      <div>
        <label>End Latitude:</label>
        <input
          type="number"
          value={end.latitude}
          onChange={(e) =>
            setEnd({ ...end, latitude: parseFloat(e.target.value) })
          }
        />

        <label>End Longitude:</label>
        <input
          type="number"
          value={end.longitude}
          onChange={(e) =>
            setEnd({ ...end, longitude: parseFloat(e.target.value) })
          }
        />
      </div>

      <div>
        <label>Battery Range (miles):</label>
        <input
          type="number"
          value={batteryRange}
          onChange={(e) => setBatteryRange(parseFloat(e.target.value))}
        />
      </div>

      <button onClick={fetchRoute}>Get Route</button>

      {route && (
        <div>
          <h3>Route Details:</h3>
          <pre>{JSON.stringify(route, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default RoutePlanner;
