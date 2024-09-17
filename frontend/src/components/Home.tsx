import React, { useState } from 'react';
import { useEffect } from 'react';
import { mapNode } from '../types/mapNode';
import MapNode from './MapNode';
import RoutePlanner from './RoutePlanner';

const Home = () => {
  const [startPoint, setStartPoint] = useState<mapNode>({
    latitude: 34.05, // Los Angeles
    longitude: -118.25, // San Francisco
  });
  const [endPoint, setEndPoint] = useState<mapNode>({
    latitude: 37.77,
    longitude: -122.41,
  });
  const [batteryRange, setBatteryRange] = useState(100);

  useEffect(() => {
    setStartPoint(startPoint);
    setEndPoint(endPoint);
  }, [startPoint, endPoint]);

  return (
    <>
      <header>
        <h1>This is a map placeholder.</h1>
        <p>
          Start Location:{' '}
          <MapNode
            latitude={startPoint.latitude}
            longitude={startPoint.longitude}
          />
        </p>
        <p>
          End Location:{' '}
          <MapNode
            latitude={endPoint.latitude}
            longitude={endPoint.longitude}
          />
        </p>
        <p>
          <RoutePlanner
            start={startPoint}
            end={endPoint}
            batteryRange={batteryRange}
            setStart={setStartPoint}
            setEnd={setEndPoint}
            setBatteryRange={setBatteryRange}
          />
        </p>
      </header>
    </>
  );
};

export default Home;
